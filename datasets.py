import os
import idx2numpy

def load_mnist(path, kind='train', normalize=True):
    """Download mnist from kaggle"""
    labels_path = os.path.join(path, f"{kind}-labels.idx1-ubyte")
    images_path = os.path.join(path, f"{kind}-images.idx3-ubyte")

    with open(labels_path, "rb") as lbpath:
        labels = idx2numpy.convert_from_file(labels_path)

    with open(images_path, 'rb') as imgpath:
        images = idx2numpy.convert_from_file(imgpath).reshape(len(labels), 28 * 28)
    
    if normalize:
        images = images / 255.0

    return images, labels


if __name__ == "__main__":
    path = "data/MNIST"
    X_train, y_train = load_mnist(path, kind='train')
    X_test, y_test = load_mnist(path, kind='t10k')

    print("X_train shape:", X_train.shape, ", y_train shape:", y_train.shape)
    print("X_test shape:", X_test.shape, ", y_test shape:", y_test.shape)
