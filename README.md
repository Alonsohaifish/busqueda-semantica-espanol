# Búsqueda semántica en español

Proyecto enfocado en la búsqueda de textos por significado y no sólo por palabras clave. 

---

## Objetivo

Preparar textos en embeddings para usarlos con FAISS en una búsqueda eficiente y encontrar textos más similares semánticamente. 

---
## Instalación

Clona el repositorio:

```bash
gh repo clone Alonsohaifish/busqueda-semantica-espanol
cd proyecto-limpieza-texto
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```


## Estructura del proyecto

```

proyecto-limpieza-texto/
```
│
├── data/
│   ├── df_tota.csv/              # Datos originales
│   
│
├── notebooks/            # Exploración y pruebas
│
├── src/
│   ├── __init__.py       
│   └── load_data.py   
│   └── embeddings.py 
│   └── index.py 
│   └── search.py 
│
├── main.py               # Script principal
├── requirements.txt
└── README.md

```

---


## Uso

Ejecuta el script principal:

```bash
python main.py
```

Esto:

1. Carga el texto desde `data/raw/`
2. Aplica limpieza
3. Procesa el texto con spaCy
4. Guarda el resultado en `data/processed/`

---

##  Ejemplo de lematización

### Entrada:

```
Y después torció bruscamente hacia abajo, tan bruscamente que Alicia no tuvo siquiera tiempo
```

### Salida:

```
['tunel', 'torcer', 'bruscamente', 'abajo', 'bruscamente', 'alicia', 'siquiera', 'tiempo', 'pensar']
```

---

## Tecnologías usadas

* Sentece Transformers
* FAISS
* Python
* unidecode

---

## Autor

Proyecto desarrollado por [Alonso Guerrero]

---

## Licencia

Este proyecto es de uso educativo y libre.
