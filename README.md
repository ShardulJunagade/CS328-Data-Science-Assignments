# CS328 Data Science Assignments

This repository contains assignments for the CS328 Introduction to Data Science course . Each assignment focuses on different aspects of data science, including network analysis, clustering, and more.


<!-- 
## Repository Structure

- **Assignment-1.ipynb**: Jupyter notebook for Assignment 1.
- **Assignment-2.ipynb**: Jupyter notebook for Assignment 2.
- **ml_publication_trends.ipynb**: Writing assignment analyzing publication trends in top AI/ML conferences (NeurIPS, ICML, ICLR) from 2006–2024, including data cleaning, LLM-based affiliation extraction, and in-depth quantitative analysis of geographic, institutional, and industry trends.
- **datasets.py**: Script for loading and processing datasets.
- **assets/**: Contains visualizations and data files for the assignments.
- **Tasks/**: Contains homework PDFs for the course.
- **old/**: Archive of older versions of assignments and questions.
 -->



<!-- ## Getting Started
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required dependencies:
   ```bash
   pip install uv
   uv venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   uv pip install -r requirements.txt
   ```
3. Open the Jupyter notebooks to explore the assignments and their solutions.
 -->



## Assignments Overview

### Assignment 1 : [Link](Assignment-1.ipynb)
Focuses on foundational data science concepts and techniques, including:
- Implementing clustering algorithms such as k-means and k-center.
- Analyzing clustering objectives and their cost functions.
- Exploring theoretical aspects of Markov's inequality and its applications.
- Working with the MNIST dataset for clustering and evaluating performance using metrics like Rand Index.

### Assignment 2 : [Link](Assignment-2.ipynb)
Covers advanced data science topics such as:
- **Q1**: Network analysis using the Facebook Large dataset.
- **Q2**: Email network analysis using adjacency matrices.
- **Q3**: K-means and K-median clustering on 1D Gaussian mixture data.
- **Q4**: Bloom filter implementation for set membership testing.

### Writing Assignment: [ML Publication Trends](ml_publication_trends.ipynb)
This writing assignment presents a comprehensive analysis of publication trends in top AI/ML conferences (NeurIPS, ICML, ICLR) from 2006–2024. It covers:
- Data cleaning and preparation, including LLM-based extraction and standardization of institution, country, and affiliation type from unstructured author affiliations.
- Quantitative analysis of growth, geographic shifts, industry involvement, institutional concentration, and collaboration trends in AI research.
- Interactive visualizations and in-depth discussion of findings, limitations, and the evolution of the global AI research landscape.



## Datasets

The datasets used in the assignments and writing project:
- **[Facebook Large](https://snap.stanford.edu/data/facebook-large-page-page-network.html)**: A dataset for social network analysis.
- **[Email-EU-core](https://snap.stanford.edu/data/email-Eu-core.html)**: A network dataset for email communication.
- **[MNIST](http://yann.lecun.com/exdb/mnist/)**: A dataset for image classification tasks.
- **[ML Publication Trends Dataset](https://github.com/martenlienen/icml-neurips-iclr-dataset)**: This dataset contains comprehensive metadata for papers published at major AI/ML conferences, including all paper titles, authors, and their affiliations for the following years:
   - **ICML**: 2017–2024
   - **NeurIPS**: 2006–2024
   - **ICLR**: 2018–2024 (excluding 2020)




## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.