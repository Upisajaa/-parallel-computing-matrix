from multiprocessing import Process, Array
import numpy as np


def add_row(A, B, C, row, cols):
    for j in range(cols):
        C[row * cols + j] = A[row][j] + B[row][j]


if __name__ == "__main__":

    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[5, 6],
                  [7, 8]])

    rows, cols = A.shape

    C = Array('i', rows * cols)

    processes = []

    # Parallel process
    for i in range(rows):
        p = Process(target=add_row, args=(A, B, C, i, cols))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    result = np.array(C[:]).reshape(rows, cols)

    print("Hasil Penjumlahan Matrix:")
    print(result)