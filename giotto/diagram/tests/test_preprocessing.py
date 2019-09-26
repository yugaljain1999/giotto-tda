"""Testing for DiagramStacker and DiagramScaler"""

import numpy as np
import pytest
from sklearn.exceptions import NotFittedError

from giotto.diagram import DiagramStacker, DiagramScaler

X_1 = {
    0: np.array([[[0., 0.36905774],
                  [0., 0.37293977],
                  [0., 0.38995215],
                  [0., 3.00457644],
                  [0., 3.04772496],
                  [0., 3.32096624]],
                 [[0., 0.36905774],
                  [0., 0.37293977],
                  [0., 0.38995215],
                  [0., 3.00457644],
                  [0., 3.04772496],
                  [0., 3.32096624]],
                 [[0., 1.32215321],
                  [0., 1.48069561],
                  [0., 1.62762213],
                  [0., 3.18582344],
                  [0., 3.25349188],
                  [0., 3.28288555]],
                 [[0., 0.13842253],
                  [0., 0.13912651],
                  [0., 0.15125643],
                  [0., 3.30339432],
                  [0., 3.3078723],
                  [0., 3.33029914]],
                 [[0., 0.13842253],
                  [0., 0.13912651],
                  [0., 0.15125643],
                  [0., 2.91534185],
                  [0., 2.93620634],
                  [0., 3.00776553]],
                 [[0., 0.13842253],
                  [0., 0.13912651],
                  [0., 0.15125643],
                  [0., 2.91534185],
                  [0., 2.93620634],
                  [0., 3.00776553]]]),
    1: np.array([[[7.97852135, 8.00382805],
                  [1.79289687, 1.8224113],
                  [1.69005811, 2.32093406],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[15.27686119,
                   24.32133484],
                  [1.79289687, 1.8224113],
                  [1.69005811, 2.32093406],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[3.32096624,
                   23.92891693],
                  [2.93474603, 3.07139683],
                  [2.83503842, 2.94497037],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[16.82829285,
                   16.84351158],
                  [16.8180275,
                   16.84162521],
                  [16.80234337,
                   16.80629158],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[2.85910106, 3.39503384],
                  [1.25564897, 1.25871313],
                  [1.24251938, 1.27403092],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[21.34438705,
                   24.6866188],
                  [2.85910106, 2.88541412],
                  [1.52559161, 3.39503384],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]]]),
    2: np.array([[[0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[25.24895287,
                   25.36620903],
                  [25.15629959,
                   25.18988037],
                  [25.06381798,
                   25.23542404],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[24.84643745,
                   25.06381798],
                  [24.77123451,
                   25.04314995],
                  [24.67935562,
                   24.93212509],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[3.66717434,
                   3.69763446],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[25.05523109,
                   25.27045441],
                  [24.93939018,
                   25.25673294],
                  [24.89836693,
                   25.20828819],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]]])
}

X_2 = {
    0: np.array([[[0., 0.36905774],
                  [0., 0.37293977],
                  [0., 0.38995215],
                  [0., 3.00457644],
                  [0., 3.32096624]],
                 [[0., 0.36905774],
                  [0., 0.37293977],
                  [0., 3.00457644],
                  [0., 3.04772496],
                  [0., 3.32096624]],
                 [[0., 1.32215321],
                  [0., 1.48069561],
                  [0., 3.18582344],
                  [0., 3.25349188],
                  [0., 3.28288555]],
                 [[0., 0.13842253],
                  [0., 0.13912651],
                  [0., 0.15125643],
                  [0., 3.3078723],
                  [0., 3.33029914]],
                 [[0., 0.13842253],
                  [0., 0.13912651],
                  [0., 0.15125643],
                  [0., 2.93620634],
                  [0., 3.00776553]],
                 [[0., 0.13842253],
                  [0., 0.13912651],
                  [0., 0.15125643],
                  [0., 2.93620634],
                  [0., 3.00776553]]]),
    1: np.array([[[7.97852135, 8.00382805],
                  [1.79289687, 1.8224113],
                  [1.69005811, 2.32093406],
                  [0., 0.],
                  [0., 0.]],
                 [[15.27686119,
                   24.32133484],
                  [1.79289687, 1.8224113],
                  [1.69005811, 2.32093406],
                  [0., 0.],
                  [0., 0.]],
                 [[3.32096624,
                   23.92891693],
                  [2.93474603, 3.07139683],
                  [2.83503842, 2.94497037],
                  [0., 0.],
                  [0., 0.]],
                 [[16.82829285,
                   16.84351158],
                  [16.8180275,
                   16.84162521],
                  [16.80234337,
                   16.80629158],
                  [0., 0.],
                  [0., 0.]],
                 [[2.85910106, 3.39503384],
                  [1.25564897, 1.25871313],
                  [1.24251938, 1.27403092],
                  [0., 0.],
                  [0., 0.]],
                 [[21.34438705,
                   24.6866188],
                  [2.85910106, 2.88541412],
                  [1.52559161, 3.39503384],
                  [0., 0.],
                  [0., 0.]]]),
    2: np.array([[[0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[25.24895287,
                   25.36620903],
                  [25.15629959,
                   25.18988037],
                  [25.06381798,
                   25.23542404],
                  [0., 0.],
                  [0., 0.]],
                 [[24.84643745,
                   25.06381798],
                  [24.77123451,
                   25.04314995],
                  [24.67935562,
                   24.93212509],
                  [0., 0.],
                  [0., 0.]],
                 [[0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[3.66717434,
                   3.69763446],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.],
                  [0., 0.]],
                 [[25.05523109,
                   25.27045441],
                  [24.93939018,
                   25.25673294],
                  [24.89836693,
                   26.20828819],
                  [0., 0.],
                  [0., 0.]]])
}


def test_not_fitted():
    dst = DiagramStacker()
    dsc = DiagramScaler()

    with pytest.raises(NotFittedError):
        dst.transform(X_1)

    with pytest.raises(NotFittedError):
        dsc.transform(X_1)

    with pytest.raises(NotFittedError):
        dsc.inverse_transform(X_1)


@pytest.mark.parametrize('X', [X_1, X_2])
def test_dst_transform(X):
    dst = DiagramStacker()
    X_res = dst.fit_transform(X)
    assert X_res[None].shape == (X[0].shape[0],
                                 len(X.keys()) * X[0].shape[1], 2)


parameters = [('wasserstein', {'order': 2, 'delta': 0.1}),
              ('betti', {'n_sampled_values': 10}),
              ('bottleneck', None)]


@pytest.mark.parametrize(('metric', 'metric_params'), parameters)
@pytest.mark.parametrize('X', [X_1, X_2])
def test_dd_transform(X, metric, metric_params):
    dsc = DiagramScaler(metric=metric, metric_params=metric_params, n_jobs=1)
    X_res = dsc.fit_transform(X)
    for i in range(len(X_1.keys())):
        assert X_res[i].shape == X[i].shape

    dsc = DiagramScaler(metric=metric, metric_params=metric_params, n_jobs=1)
    X_inv_res = dsc.fit(X_res).inverse_transform(X_res)
    for i in range(len(X_inv_res.keys())):
        assert X_inv_res[i].shape == X[i].shape
