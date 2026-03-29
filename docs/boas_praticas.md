# Guia de Boas Práticas - Ciência de Dados

Este documento contém diretrizes e boas práticas para o desenvolvimento de projetos de ciência de dados.

## 📋 Estrutura de Código

### Organização de Notebooks

```python
# 1. Importações
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Configurações
pd.set_option('display.max_columns', None)
plt.style.use('seaborn')
sns.set_palette("husl")

# 3. Constantes
RANDOM_STATE = 42
TEST_SIZE = 0.2

# 4. Código principal
# ...
```

### Convenções de Nomenclatura

- **Variáveis**: `snake_case` (ex: `dados_clientes`, `modelo_final`)
- **Constantes**: `UPPER_CASE` (ex: `RANDOM_STATE`, `MAX_FEATURES`)
- **Funções**: `snake_case` (ex: `calcular_media()`, `preparar_dados()`)
- **Classes**: `PascalCase` (ex: `ModeloPredicao`, `ProcessadorDados`)

## 🔍 Análise Exploratória de Dados (EDA)

### Checklist Básico

1. **Visão Geral dos Dados**
```python
df.head()
df.info()
df.describe()
df.shape
```

2. **Valores Ausentes**
```python
df.isnull().sum()
df.isnull().sum() / len(df) * 100  # Percentual
```

3. **Valores Únicos**
```python
df.nunique()
df['coluna'].value_counts()
```

4. **Estatísticas por Grupo**
```python
df.groupby('categoria').agg(['mean', 'median', 'std'])
```

### Visualizações Recomendadas

- **Distribuições**: Histogramas, box plots
- **Relações**: Scatter plots, pair plots
- **Categóricas**: Bar plots, count plots
- **Temporais**: Line plots
- **Correlações**: Heatmaps

## 🛠️ Pré-processamento de Dados

### Tratamento de Valores Ausentes

```python
# Remover linhas com valores ausentes
df.dropna()

# Preencher com média/mediana
df.fillna(df.mean())

# Preencher com valor específico
df.fillna(0)

# Forward/Backward fill (séries temporais)
df.fillna(method='ffill')
```

### Tratamento de Outliers

```python
# Método IQR
Q1 = df['coluna'].quantile(0.25)
Q3 = df['coluna'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrar outliers
df_sem_outliers = df[(df['coluna'] >= limite_inferior) & 
                      (df['coluna'] <= limite_superior)]
```

### Encoding de Variáveis Categóricas

```python
# One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=['categoria'])

# Label Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['categoria_encoded'] = le.fit_transform(df['categoria'])
```

### Normalização/Padronização

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Padronização (Z-score)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[colunas_numericas])

# Normalização (0-1)
scaler = MinMaxScaler()
df_normalized = scaler.fit_transform(df[colunas_numericas])
```

## 📊 Visualização de Dados

### Princípios Básicos

1. **Clareza**: Gráficos devem ser fáceis de entender
2. **Relevância**: Mostrar apenas informações importantes
3. **Precisão**: Escala e proporções corretas
4. **Estética**: Design limpo e profissional

### Personalização de Gráficos

```python
# Configuração padrão
plt.figure(figsize=(10, 6))
plt.title('Título do Gráfico', fontsize=14, fontweight='bold')
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
```

## 🤖 Machine Learning

### Divisão de Dados

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

### Validação Cruzada

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(modelo, X_train, y_train, cv=5)
print(f"Acurácia média: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### Métricas de Avaliação

**Classificação**:
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
```

**Regressão**:
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

## 📝 Documentação

### Comentários em Código

```python
# BOM: Explicar o "porquê"
# Removemos outliers usando IQR pois os dados têm distribuição assimétrica
df_clean = remove_outliers_iqr(df, 'preco')

# RUIM: Explicar o "o quê" (óbvio pelo código)
# Remove outliers
df_clean = remove_outliers_iqr(df, 'preco')
```

### Markdown em Notebooks

Use células markdown para:
- Títulos de seções
- Explicações de análises
- Interpretação de resultados
- Conclusões e insights

## 🔐 Segurança e Privacidade

1. **Nunca commitar credenciais** (use variáveis de ambiente)
2. **Anonimizar dados sensíveis** antes de compartilhar
3. **Usar .gitignore** para arquivos de dados grandes
4. **Documentar fontes de dados** e permissões de uso

## 🚀 Performance

### Dicas de Otimização

```python
# Usar tipos de dados apropriados
df['categoria'] = df['categoria'].astype('category')
df['inteiro'] = df['inteiro'].astype('int32')

# Operações vetorizadas (evitar loops)
# RUIM
resultado = [x * 2 for x in df['coluna']]
# BOM
resultado = df['coluna'] * 2

# Usar chunking para arquivos grandes
for chunk in pd.read_csv('arquivo_grande.csv', chunksize=10000):
    processar(chunk)
```

## 📚 Recursos Adicionais

- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [Pandas Best Practices](https://pandas.pydata.org/docs/user_guide/gotchas.html)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Data Science Best Practices](https://www.datacamp.com/community/tutorials/data-science-best-practices)

---

**Lembre-se**: Código limpo e bem documentado é tão importante quanto análises corretas!
