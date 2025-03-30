# CS328 Data Science Assignments

This repository contains assignments for the CS328 Introduction to Data Science course. Each assignment focuses on different aspects of data science, including network analysis, clustering, and more.

## Repository Structure

- **Assignment-1.ipynb**: Jupyter notebook for Assignment 1.
- **Assignment-2.ipynb**: Jupyter notebook for Assignment 2.
- **datasets.py**: Script for loading and processing datasets.
- **assets/**: Contains visualizations and data files for the assignments.
- **Tasks/**: Contains homework PDFs for the course.
<!-- - **old/**: Archive of older versions of assignments and questions. -->

## How to Use

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

## Datasets

The datasests used in the assignments:
- **[Facebook Large](https://snap.stanford.edu/data/facebook-large-page-page-network.html)**: A dataset for social network analysis.
- **[Email-EU-core](https://snap.stanford.edu/data/email-Eu-core.html)**: A network dataset for email communication.
- **[MNIST](http://yann.lecun.com/exdb/mnist/)**: A dataset for image classification tasks.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.