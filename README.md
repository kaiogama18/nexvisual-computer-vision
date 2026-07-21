# Fundamentos de Visão Computacional

Bem-vindo(a) a este repositório! 

Este repositório reúne **Os exercícios, desafios e projetos desenvolvidos ao longo do curso de Fundamentos de Visão Computacional**, servindo como material de apoio para estudos, consultas e evolução prática dos conteúdos apresentados em cada módulo.

---

#  Estrutura do Repositório

Cada pasta corresponde a um módulo do curso e contém:

-  Exercícios propostos
-  Desafios práticos
-  Projetos desenvolvidos

```
Módulos
├── Módulo 1 - Tópicos específicos em programação aplicados a visão computacional
├── Módulo 2 - Tópicos em aprendizagem de máquina
├── Módulo 3 - Redes neurais convolucionais
├── Módulo 4 - Modelos gerativos
├── Módulo 5 - Projetos reais de visão computacional
└── Módulo 6 - ML OPS
```

---

# Objetivos deste Repositório

- Centralizar todos os exercícios do curso.
- Documentar os desafios resolvidos em cada módulo.
- Compartilhar projetos práticos desenvolvidos durante a formação.
- Servir como material de consulta para estudos futuros.
- Acompanhar a evolução ao longo da jornada em Visão Computacional.

---

#  Tecnologias Utilizadas

- Python
- NumPy
- Pandas
- OpenCV
- Matplotlib
- Scikit-Learn
- TensorFlow
- Keras
- PyTorch
- Jupyter Notebook

# Projeto 1 – Extração de Movimento para Blender

## Objetivo

Extrair os movimentos de uma pessoa a partir de um vídeo e converter essas informações em uma animação que possa ser utilizada no Blender.

## Fluxo do Projeto

1. Processar um vídeo para detectar a pose humana quadro a quadro.
2. Extrair as coordenadas das articulações (keypoints).
3. Gerar um arquivo no formato **JSON** contendo toda a sequência da animação.
4. Importar o arquivo JSON no Blender.
5. Criar automaticamente o esqueleto (Armature).
6. Aplicar as animações ao esqueleto utilizando os dados do JSON.

## Resultado Esperado

* Extração automática de movimentos humanos.
* Arquivo JSON compatível com o pipeline do Blender.
* Geração automática do rig e da animação.
* Facilidade para reutilizar movimentos em diferentes personagens.

  

https://github.com/user-attachments/assets/cbe6e55f-4dc4-457d-bacf-d6017afe7e08




# Projeto 2 – Detecção de Buracos em Ruas

## Objetivo

Treinar um modelo capaz de detectar buracos em vias públicas e utilizá-lo em tempo real em dispositivos Android.

## Fluxo do Projeto

1. Coletar e organizar um conjunto de imagens contendo ruas com e sem buracos.
2. Treinar um modelo de detecção de objetos.
3. Validar o desempenho do modelo.
4. Converter o modelo treinado para o formato **TensorFlow Lite (Float16)**.
5. Gerar o arquivo:

```
best_float16.tflite
```

6. Integrar o modelo ao aplicativo Android.
7. Utilizar a câmera do dispositivo para detectar buracos em tempo real.

## Resultado Esperado

* Modelo otimizado para dispositivos móveis.
* Inferência em tempo real utilizando a câmera.
* Baixo consumo de memória e processamento.
* Arquivo `.tflite` pronto para implantação em aplicações Android.
