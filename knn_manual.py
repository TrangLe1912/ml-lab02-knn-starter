"""LAB 02 - KNN from scratch.

Hoàn thiện các hàm trong file này mà KHÔNG dùng sklearn.neighbors.
Bạn có thể dùng Python chuẩn và NumPy.
"""

from collections import Counter
from math import sqrt


def euclidean_distance(x, y):
    """Trả về Euclidean distance giữa hai vector cùng số chiều.

    Parameters
    ----------
    x, y : iterable of numbers

    Returns
    -------
    float
    """
    # TODO: Mission 1
    raise NotImplementedError("Complete euclidean_distance()")


def manhattan_distance(x, y):
    """Trả về Manhattan distance giữa hai vector cùng số chiều."""
    # TODO: Mission 1
    raise NotImplementedError("Complete manhattan_distance()")


def get_k_neighbors(X_train, y_train, sample, k=3, metric="euclidean"):
    """Tìm K hàng xóm gần sample nhất.

    Parameters
    ----------
    X_train : array-like, shape (n_samples, n_features)
    y_train : array-like, shape (n_samples,)
    sample : array-like, shape (n_features,)
    k : int
    metric : {'euclidean', 'manhattan'}

    Returns
    -------
    list[tuple]
        Danh sách đã sắp xếp theo khoảng cách tăng dần.
        Mỗi phần tử có dạng: (index, distance, label)

    Gợi ý
    -----
    1. Chọn hàm distance theo metric.
    2. Tính distance từ sample tới từng row trong X_train.
    3. Lưu (index, distance, label).
    4. Sort theo (distance, index) để tie có kết quả xác định.
    5. Trả về K phần tử đầu tiên.
    """
    # TODO: Mission 2
    raise NotImplementedError("Complete get_k_neighbors()")


def knn_predict_one(X_train, y_train, sample, k=3, metric="euclidean"):
    """Dự đoán nhãn cho một sample bằng majority vote.

    Trong lab chính, ưu tiên K lẻ để hạn chế hòa phiếu.
    """
    # TODO: Mission 2
    raise NotImplementedError("Complete knn_predict_one()")
