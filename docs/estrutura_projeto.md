# Estrutura do Projeto - Visão Geral

## 📁 Organização Atual

Este documento descreve a estrutura organizacional do repositório após a reorganização.

### Estrutura de Diretórios

```
Ciencia_de_dados_Ebac/
│
├── README.md                    # Documentação principal do projeto
├── requirements.txt             # Dependências Python do projeto
├── .gitignore                   # Arquivos e pastas ignorados pelo Git
│
├── modulos/                     # Módulos do curso organizados por tema
│   │
│   ├── modulo_03_python_basico/
│   │   ├── README.md           # Documentação específica do módulo
│   │   ├── *.ipynb             # Notebooks do módulo
│   │   └── exercicios/         # Exercícios práticos (.py e .ipynb)
│   │
│   ├── modulo_04_python/
│   │   ├── README.md
│   │   ├── *.ipynb
│   │   └── exercicios/
│   │
│   ├── modulo_05_estatistica/
│   │   ├── README.md
│   │   ├── *.ipynb
│   │   └── exercicios/
│   │
│   ├── modulo_06_analise_dados/
│   │   ├── README.md
│   │   ├── *.ipynb
│   │   └── exercicios/
│   │
│   └── modulo_07_analise_dados_avancada/
│       ├── README.md
│       ├── *.ipynb
│       └── exercicios/
│
├── projetos/                    # Projetos práticos completos
│   ├── README.md               # Documentação dos projetos
│   ├── Projeto 01 - Classificação de crédito.ipynb
│   ├── Ebac_Project.ipynb
│   └── demo01.ipynb
│
└── docs/                        # Documentação adicional
    ├── boas_praticas.md        # Guia de boas práticas
    └── CONTRIBUTING.md         # Guia de contribuição
```

## 🎯 Princípios de Organização

### 1. Modularidade
- Cada módulo do curso tem sua própria pasta
- Facilita localização de conteúdo específico
- Permite crescimento independente de cada módulo

### 2. Separação de Conteúdo
- **Módulos**: Material de aprendizado estruturado
- **Projetos**: Aplicações práticas completas
- **Docs**: Documentação e guias

### 3. Nomenclatura Consistente
- Pastas em `snake_case` minúsculo
- Nomes descritivos e em português
- Convenções mantidas em todo o projeto

### 4. Documentação em Camadas
- **README.md principal**: Visão geral do repositório
- **README.md por módulo**: Detalhes específicos
- **docs/**: Guias e documentação adicional

## 📋 Convenções de Nomenclatura

### Arquivos
- **Notebooks principais**: Nome descritivo do conteúdo
- **Exercícios Python**: `Lab##_ex##.py` ou nome descritivo
- **Documentação**: `README.md`, `CONTRIBUTING.md`, etc.

### Diretórios
- **Módulos**: `modulo_##_nome_descritivo`
- **Subpastas**: `exercicios`, `dados`, etc.
- Sempre em minúsculas com underscore

## 🔍 Navegação Rápida

### Para Iniciantes
1. Comece pelo [README.md](../README.md) principal
2. Explore os módulos em ordem (03 → 07)
3. Cada módulo tem seu próprio README com orientações

### Para Buscar Conteúdo Específico

**Python Básico**:
- `modulos/modulo_03_python_basico/`

**Estatística**:
- `modulos/modulo_05_estatistica/`

**Análise de Dados**:
- `modulos/modulo_06_analise_dados/`
- `modulos/modulo_07_analise_dados_avancada/`

**Projetos Completos**:
- `projetos/`

**Guias e Documentação**:
- `docs/boas_praticas.md`: Boas práticas de programação
- `docs/CONTRIBUTING.md`: Como contribuir

## 📊 Tipos de Arquivos

### `.ipynb` (Jupyter Notebooks)
- Material principal de aprendizado
- Contém código, explicações e visualizações
- Executar com `jupyter notebook`

### `.py` (Scripts Python)
- Exercícios práticos
- Scripts auxiliares
- Executar com `python arquivo.py`

### `.md` (Markdown)
- Documentação
- Guias e tutoriais
- Instruções e explicações

### `.txt` (Texto)
- `requirements.txt`: Lista de dependências

## 🚀 Fluxo de Trabalho Recomendado

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/DDricko/Ciencia_de_dados_Ebac.git
   cd Ciencia_de_dados_Ebac
   ```

2. **Configurar ambiente**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. **Estudar por módulo**
   - Abrir README do módulo
   - Seguir ordem dos notebooks
   - Fazer exercícios na pasta `exercicios/`

4. **Praticar com projetos**
   - Após concluir módulos relevantes
   - Aplicar conhecimentos aprendidos
   - Experimentar variações

## 🔄 Manutenção e Atualizações

### Adicionar Novo Módulo
1. Criar pasta `modulos/modulo_##_nome/`
2. Adicionar `README.md` descritivo
3. Criar subpasta `exercicios/`
4. Atualizar README principal

### Adicionar Novo Projeto
1. Adicionar notebook em `projetos/`
2. Documentar no `projetos/README.md`
3. Atualizar README principal se necessário

### Atualizar Dependências
1. Adicionar/modificar em `requirements.txt`
2. Testar instalação
3. Documentar mudanças se significativas

## ✅ Benefícios da Nova Estrutura

1. **Fácil Navegação**: Estrutura clara e intuitiva
2. **Escalável**: Fácil adicionar novo conteúdo
3. **Documentada**: Cada seção tem orientações
4. **Profissional**: Segue padrões da indústria
5. **Educacional**: Facilita o aprendizado progressivo
6. **Manutenível**: Fácil de manter e atualizar

## 📚 Recursos Adicionais

- [Git Workflow](https://guides.github.com/introduction/flow/)
- [Jupyter Notebook Tips](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
- [Python Project Structure](https://docs.python-guide.org/writing/structure/)

---

**Última atualização**: Janeiro 2026
