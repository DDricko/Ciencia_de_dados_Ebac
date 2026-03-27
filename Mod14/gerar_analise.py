#!/usr/bin/env python3
"""
Script para gerar análises automáticas dos dados SINASC por mês
Uso: python gerar_analise.py MAR ABR MAI JUN JUL

Gera diretórios estruturados (2019-03, 2019-04, etc.) e gráficos de análise temporal
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import argparse
from pathlib import Path

# Configurações globais
plt.style.use('default')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 10

# Mapeamento de meses
MESES_MAP = {
    'JAN': {'num': '01', 'nome': 'Janeiro', 'ordem': 1},
    'FEV': {'num': '02', 'nome': 'Fevereiro', 'ordem': 2},
    'MAR': {'num': '03', 'nome': 'Março', 'ordem': 3},
    'ABR': {'num': '04', 'nome': 'Abril', 'ordem': 4},
    'MAI': {'num': '05', 'nome': 'Maio', 'ordem': 5},
    'JUN': {'num': '06', 'nome': 'Junho', 'ordem': 6},
    'JUL': {'num': '07', 'nome': 'Julho', 'ordem': 7},
    'AGO': {'num': '08', 'nome': 'Agosto', 'ordem': 8},
    'SET': {'num': '09', 'nome': 'Setembro', 'ordem': 9},
    'OUT': {'num': '10', 'nome': 'Outubro', 'ordem': 10},
    'NOV': {'num': '11', 'nome': 'Novembro', 'ordem': 11},
    'DEZ': {'num': '12', 'nome': 'Dezembro', 'ordem': 12}
}

class GeradorAnalise:
    def __init__(self, meses_lista, diretorio_dados='input', ano=2019):
        """
        Inicializa o gerador de análise
        
        Args:
            meses_lista: Lista de abreviaturas de meses (ex: ['MAR', 'ABR', 'MAI'])
            diretorio_dados: Diretório contendo os arquivos CSV
            ano: Ano de referência dos dados
        """
        self.meses_lista = sorted(meses_lista, key=lambda x: MESES_MAP[x]['ordem'])
        self.diretorio_dados = diretorio_dados
        self.ano = ano
        self.dados_carregados = {}
        self.diretorio_base = Path(f"analise_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        
        print(f"🚀 Iniciando análise para os meses: {', '.join(self.meses_lista)}")
        print(f"📁 Diretório base: {self.diretorio_base}")

    def carregar_dados(self):
        """Carrega dados dos arquivos CSV para os meses especificados"""
        print("\n📂 Carregando dados dos arquivos CSV...")
        
        for mes in self.meses_lista:
            arquivo = f"{self.diretorio_dados}/SINASC_RO_{self.ano}_{mes}.csv"
            
            if os.path.exists(arquivo):
                try:
                    df = pd.read_csv(arquivo)
                    df['MES_CODIGO'] = mes
                    df['MES_NUMERO'] = MESES_MAP[mes]['num']
                    df['MES_NOME'] = MESES_MAP[mes]['nome']
                    
                    # Converter data de nascimento
                    df['DTNASC'] = pd.to_datetime(df['DTNASC'], errors='coerce')
                    
                    self.dados_carregados[mes] = df
                    print(f"✅ {MESES_MAP[mes]['nome']}: {len(df):,} registros")
                    
                except Exception as e:
                    print(f"❌ Erro ao carregar {arquivo}: {e}")
            else:
                print(f"⚠️ Arquivo não encontrado: {arquivo}")
                
        print(f"\n📊 Total de datasets carregados: {len(self.dados_carregados)}")

    def criar_diretorios(self):
        """Cria a estrutura de diretórios para cada mês"""
        print("\n📁 Criando estrutura de diretórios...")
        
        # Criar diretório base
        self.diretorio_base.mkdir(exist_ok=True)
        
        for mes in self.meses_lista:
            if mes in self.dados_carregados:
                mes_dir = self.diretorio_base / f"{self.ano}-{MESES_MAP[mes]['num']}"
                mes_dir.mkdir(exist_ok=True)
                
                # Criar subdiretórios
                (mes_dir / "graficos").mkdir(exist_ok=True)
                (mes_dir / "dados").mkdir(exist_ok=True)
                (mes_dir / "relatorios").mkdir(exist_ok=True)
                
                print(f"✅ Criado: {mes_dir}")

    def gerar_timeline_visual(self, mes_atual):
        """Gera visualização de linha temporal até o mês atual"""
        # Meses desde janeiro até o mês atual
        meses_timeline = []
        for mes_código, info in MESES_MAP.items():
            if info['ordem'] <= MESES_MAP[mes_atual]['ordem']:
                meses_timeline.append(mes_código)
        
        # Criar figura
        fig, ax = plt.subplots(1, 1, figsize=(16, 4))
        fig.patch.set_facecolor('#f0f0f0')
        
        # Título principal
        ax.text(0.5, 0.9, f'{self.ano}', ha='center', va='center', 
                transform=ax.transAxes, fontsize=36, fontweight='bold', 
                color='white', bbox=dict(boxstyle="round,pad=0.1", 
                facecolor='#4472C4', edgecolor='none', alpha=0.9))
        
        # Desenhar blocos dos meses
        num_meses = len(meses_timeline)
        largura_bloco = 0.8 / num_meses if num_meses > 0 else 0.1
        spacing = 0.02
        
        for i, mes in enumerate(meses_timeline):
            x_pos = 0.1 + i * (largura_bloco + spacing)
            
            # Determinar cor (destaque no mês atual)
            if mes == mes_atual:
                cor = '#FF6B6B'  # Cor destacada para o mês atual
                alpha = 1.0
            else:
                cor = '#4472C4'  # Cor padrão
                alpha = 0.8
                
            # Desenhar bloco do mês
            rect = plt.Rectangle((x_pos, 0.3), largura_bloco, 0.3, 
                               facecolor=cor, edgecolor='white', 
                               linewidth=2, alpha=alpha)
            ax.add_patch(rect)
            
            # Texto do mês
            ax.text(x_pos + largura_bloco/2, 0.45, mes, 
                   ha='center', va='center', fontsize=14, 
                   fontweight='bold', color='white')
        
        # Seta apontando para o mês atual
        if mes_atual in meses_timeline:
            idx_atual = meses_timeline.index(mes_atual)
            x_seta = 0.1 + idx_atual * (largura_bloco + spacing) + largura_bloco/2
            ax.annotate('', xy=(x_seta, 0.25), xytext=(x_seta, 0.1),
                       arrowprops=dict(arrowstyle='->', lw=3, color='#FF6B6B'))
        
        # Configurar eixos
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        plt.tight_layout()
        return fig

    def gerar_estatisticas_mes(self, mes):
        """Gera gráficos de estatísticas para um mês específico"""
        if mes not in self.dados_carregados:
            print(f"⚠️ Dados não encontrados para {mes}")
            return
            
        df = self.dados_carregados[mes]
        mes_dir = self.diretorio_base / f"{self.ano}-{MESES_MAP[mes]['num']}"
        
        # 1. Distribuição por sexo
        if 'SEXO' in df.columns:
            fig, axes = plt.subplots(2, 2, figsize=(15, 12))
            fig.suptitle(f'Análise dos Nascimentos - {MESES_MAP[mes]["nome"]} {self.ano}', 
                        fontsize=16, fontweight='bold')
            
            # Sexo
            sexo_counts = df['SEXO'].value_counts()
            axes[0,0].pie(sexo_counts.values, labels=sexo_counts.index, autopct='%1.1f%%',
                         colors=['lightblue', 'pink'])
            axes[0,0].set_title('Distribuição por Sexo')
            
            # Peso
            if 'PESO' in df.columns:
                df['PESO'].hist(bins=30, ax=axes[0,1], color='lightgreen', alpha=0.7)
                axes[0,1].set_title('Distribuição do Peso dos Bebês')
                axes[0,1].set_xlabel('Peso (gramas)')
                axes[0,1].axvline(df['PESO'].mean(), color='red', linestyle='--', 
                                 label=f'Média: {df["PESO"].mean():.0f}g')
                axes[0,1].legend()
            
            # Idade das mães
            if 'IDADEMAE' in df.columns:
                df['IDADEMAE'].hist(bins=20, ax=axes[1,0], color='orange', alpha=0.7)
                axes[1,0].set_title('Distribuição da Idade das Mães')
                axes[1,0].set_xlabel('Idade (anos)')
                axes[1,0].axvline(df['IDADEMAE'].mean(), color='red', linestyle='--',
                                 label=f'Média: {df["IDADEMAE"].mean():.1f} anos')
                axes[1,0].legend()
            
            # APGAR 5 minutos
            if 'APGAR5' in df.columns:
                apgar_counts = df['APGAR5'].value_counts().sort_index()
                apgar_counts.plot(kind='bar', ax=axes[1,1], color='lightcoral')
                axes[1,1].set_title('Distribuição APGAR 5º Minuto')
                axes[1,1].set_xlabel('Pontuação APGAR')
                axes[1,1].tick_params(axis='x', rotation=45)
            
            plt.tight_layout()
            plt.savefig(mes_dir / "graficos" / "estatisticas_nascimentos.png", 
                       dpi=300, bbox_inches='tight')
            plt.close()
            
        print(f"📊 Gráficos estatísticos salvos para {MESES_MAP[mes]['nome']}")

    def gerar_timeline_mes(self, mes):
        """Gera timeline visual para um mês específico"""
        mes_dir = self.diretorio_base / f"{self.ano}-{MESES_MAP[mes]['num']}"
        
        # Gerar timeline
        fig = self.gerar_timeline_visual(mes)
        
        # Salvar timeline
        fig.savefig(mes_dir / "graficos" / "timeline_visual.png", 
                   dpi=300, bbox_inches='tight', facecolor='#f0f0f0')
        plt.close()
        
        print(f"📅 Timeline visual salva para {MESES_MAP[mes]['nome']}")

    def gerar_relatorio_mes(self, mes):
        """Gera relatório textual para um mês específico"""
        if mes not in self.dados_carregados:
            return
            
        df = self.dados_carregados[mes]
        mes_dir = self.diretorio_base / f"{self.ano}-{MESES_MAP[mes]['num']}"
        
        # Gerar relatório
        relatorio = f"""
# RELATÓRIO DE ANÁLISE - {MESES_MAP[mes]['nome'].upper()} {self.ano}

## Resumo Geral
- **Total de nascimentos**: {len(df):,}
- **Data de geração**: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

## Estatísticas Principais
"""
        
        if 'PESO' in df.columns:
            relatorio += f"""
### Peso dos Bebês
- **Peso médio**: {df['PESO'].mean():.1f}g
- **Peso mínimo**: {df['PESO'].min()}g
- **Peso máximo**: {df['PESO'].max()}g
- **Desvio padrão**: {df['PESO'].std():.1f}g
"""
        
        if 'IDADEMAE' in df.columns:
            relatorio += f"""
### Idade das Mães
- **Idade média**: {df['IDADEMAE'].mean():.1f} anos
- **Idade mínima**: {df['IDADEMAE'].min()} anos
- **Idade máxima**: {df['IDADEMAE'].max()} anos
"""
        
        if 'SEXO' in df.columns:
            sexo_dist = df['SEXO'].value_counts(normalize=True) * 100
            relatorio += f"""
### Distribuição por Sexo
"""
            for sexo, pct in sexo_dist.items():
                relatorio += f"- **{sexo}**: {pct:.1f}%\n"
        
        if 'CONSULTAS' in df.columns:
            relatorio += f"""
### Consultas Pré-Natal
- **Média de consultas**: {df['CONSULTAS'].mean():.1f}
"""
        
        # Salvar relatório
        with open(mes_dir / "relatorios" / "relatorio_mensal.md", 'w', encoding='utf-8') as f:
            f.write(relatorio)
            
        print(f"📝 Relatório salvo para {MESES_MAP[mes]['nome']}")

    def exportar_dados_mes(self, mes):
        """Exporta dados processados para um mês específico"""
        if mes not in self.dados_carregados:
            return
            
        df = self.dados_carregados[mes]
        mes_dir = self.diretorio_base / f"{self.ano}-{MESES_MAP[mes]['num']}"
        
        # Exportar CSV processado
        df.to_csv(mes_dir / "dados" / "dados_processados.csv", index=False)
        
        # Exportar resumo estatístico
        resumo = df.describe()
        resumo.to_csv(mes_dir / "dados" / "resumo_estatistico.csv")
        
        print(f"💾 Dados exportados para {MESES_MAP[mes]['nome']}")

    def gerar_analise_completa(self):
        """Executa análise completa para todos os meses especificados"""
        print("\n🎯 Iniciando geração de análise completa...")
        
        # Carregar dados
        self.carregar_dados()
        
        # Criar estrutura de diretórios
        self.criar_diretorios()
        
        # Processar cada mês
        for mes in self.meses_lista:
            if mes in self.dados_carregados:
                print(f"\n📊 Processando {MESES_MAP[mes]['nome']}...")
                
                # Gerar timeline visual
                self.gerar_timeline_mes(mes)
                
                # Gerar gráficos estatísticos
                self.gerar_estatisticas_mes(mes)
                
                # Gerar relatório
                self.gerar_relatorio_mes(mes)
                
                # Exportar dados
                self.exportar_dados_mes(mes)
                
                print(f"✅ {MESES_MAP[mes]['nome']} concluído!")
        
        # Gerar relatório geral
        self.gerar_relatorio_geral()
        
        print(f"\n🎉 Análise completa finalizada! Arquivos salvos em: {self.diretorio_base}")

    def gerar_relatorio_geral(self):
        """Gera relatório geral comparativo entre todos os meses"""
        print("\n📋 Gerando relatório geral...")
        
        # Compilar estatísticas de todos os meses
        relatorio_geral = f"""
# RELATÓRIO GERAL DE ANÁLISE - {self.ano}

## Meses Analisados
{', '.join([MESES_MAP[mes]['nome'] for mes in self.meses_lista])}

## Evolução dos Nascimentos
"""
        
        total_nascimentos = 0
        for mes in self.meses_lista:
            if mes in self.dados_carregados:
                qtd = len(self.dados_carregados[mes])
                total_nascimentos += qtd
                relatorio_geral += f"- **{MESES_MAP[mes]['nome']}**: {qtd:,} nascimentos\n"
        
        relatorio_geral += f"\n**Total acumulado**: {total_nascimentos:,} nascimentos\n"
        
        relatorio_geral += f"""
## Estrutura de Arquivos Gerados
Para cada mês (2019-XX), foram criados:
- `/graficos/` - Visualizações e timeline
- `/dados/` - Dados processados em CSV
- `/relatorios/` - Relatório detalhado em Markdown

## Como Usar os Resultados
1. Abra cada diretório 2019-XX para ver os resultados específicos do mês
2. Use os gráficos em `graficos/` para apresentações
3. Consulte os relatórios em `relatorios/` para análises detalhadas
4. Os dados em `dados/` podem ser reimportados para análises adicionais
"""
        
        # Salvar relatório geral
        with open(self.diretorio_base / "RELATORIO_GERAL.md", 'w', encoding='utf-8') as f:
            f.write(relatorio_geral)
            
        print("✅ Relatório geral salvo!")


def main():
    """Função principal do script"""
    parser = argparse.ArgumentParser(
        description='Gera análises automáticas dos dados SINASC por mês',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python gerar_analise.py MAR ABR MAI JUN JUL
  python gerar_analise.py JAN FEV MAR
  python gerar_analise.py DEZ

Para cada mês especificado, será criado um diretório 2019-XX contendo:
- Gráficos estatísticos dos nascimentos
- Timeline visual mostrando evolução temporal  
- Relatórios em texto
- Dados processados em CSV
        """
    )
    
    parser.add_argument('meses', nargs='+', 
                       choices=list(MESES_MAP.keys()),
                       help='Lista de abreviaturas de meses (MAR, ABR, MAI, etc.)')
    
    parser.add_argument('--dados-dir', default='input',
                       help='Diretório contendo os arquivos CSV (padrão: input)')
    
    parser.add_argument('--ano', type=int, default=2019,
                       help='Ano de referência dos dados (padrão: 2019)')
    
    args = parser.parse_args()
    
    # Validar meses
    meses_invalidos = [mes for mes in args.meses if mes not in MESES_MAP]
    if meses_invalidos:
        print(f"❌ Meses inválidos: {', '.join(meses_invalidos)}")
        print(f"Meses válidos: {', '.join(MESES_MAP.keys())}")
        sys.exit(1)
    
    # Mostrar informações
    print("=" * 60)
    print("🚀 GERADOR DE ANÁLISE SINASC")
    print("=" * 60)
    print(f"📅 Meses selecionados: {', '.join(args.meses)}")
    print(f"📁 Diretório de dados: {args.dados_dir}")
    print(f"📆 Ano: {args.ano}")
    print("=" * 60)
    
    try:
        # Criar e executar gerador
        gerador = GeradorAnalise(args.meses, args.dados_dir, args.ano)
        gerador.gerar_analise_completa()
        
    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro durante execução: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()