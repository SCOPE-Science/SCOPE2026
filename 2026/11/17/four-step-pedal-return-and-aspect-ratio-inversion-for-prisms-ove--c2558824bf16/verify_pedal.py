"""Independent finite numerical diagnostics for the exact pedal prism identities."""
import numpy as np
from scipy.spatial import ConvexHull


def pedal(vertices):
    facets = ConvexHull(vertices).equations
    distinct = []
    for row in facets:
        if not any(np.linalg.norm(row - known, ord=np.inf) < 1e-8 for known in distinct):
            distinct.append(row)
    feet = np.array([-row[-1] * row[:-1] / np.dot(row[:-1], row[:-1]) for row in distinct])
    return feet


def compare_vertex_sets(actual, predicted):
    distances = np.linalg.norm(actual[:, None, :] - predicted[None, :, :], axis=2)
    return max(np.max(np.min(distances, axis=0)), np.max(np.min(distances, axis=1)))


def case(base, a, R, h):
    initial = np.array([np.r_[v, z] for v in base for z in (-h, h)])
    current = initial.copy()
    steps = []
    for _ in range(4):
        current = pedal(current)
        steps.append(current)
    rho2 = 1.0 / (R**2 / a**4 + 1.0 / h**2)
    predicted_two = np.array([np.r_[(rho2 / a**2) * v, (rho2 / h**2) * z]
                              for v in base for z in (-h, h)])
    s, t = R / a, h / a
    gamma = t * t / ((1 + s * s * t * t) * (s * s + t * t))
    error_two = compare_vertex_sets(steps[1], predicted_two)
    error_four = compare_vertex_sets(steps[3], gamma * initial)
    assert error_two < 2e-6 and error_four < 2e-6
    assert (s >= 1 and 0 < gamma < 1)
    print(f"m={base.shape[1]}, base_vertices={len(base)}, h/a={t:.9g}, "
          f"gamma={gamma:.12g}, two-step-error={error_two:.3g}, four-step-error={error_four:.3g}")


def main():
    n, R, h = 5, 2.0, 3.0
    pentagon = np.array([[R * np.cos(2*np.pi*j/n), R * np.sin(2*np.pi*j/n)]
                         for j in range(n)])
    case(pentagon, R * np.cos(np.pi/n), R, h)
    A, B, C = 2.0, 3.0, 4.0
    tetra = np.array([[A, B, C], [A, -B, -C], [-A, B, -C], [-A, -B, C]])
    case(tetra, 1.0 / np.sqrt(A**-2 + B**-2 + C**-2),
         np.sqrt(A*A + B*B + C*C), 1.7)
    print('Both independent finite diagnostics passed.')


if __name__ == '__main__':
    main()
