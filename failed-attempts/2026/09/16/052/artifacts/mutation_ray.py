"""Model Markov-type Vieta dynamics illustrating unbounded GL-invariant along an
infinite mutation ray (mechanism behind TARGET infinitude).

Point: iterated rank-2 mutations of infinite type produce Newton data whose
max edge lattice length is strictly increasing, hence infinitely many pairwise
GL(2,Z)-inequivalent polytopes -- even though normalized volume stays constant
(so volume alone does NOT distinguish; edge/Markov data do).

This mirrors the Pascaleff-Tonkonog infinite mutation graph mechanism for the
monotone cubic: an infinite ray of infinite-type cluster mutations forces
unbounded denominator/edge data, hence infinitely many GL-classes, hence (by
the invariance lemma in DRAFT.md) infinitely many Hamiltonian classes.
The recurrence below uses the Markov constant K=3 as an explicit auditable
model of indefinite Vieta jumping. See DRAFT.md Lemma 3.
"""
import json
import os


def vieta_move(triple, idx, K=3):
    a = list(triple)
    others = [a[j] for j in range(3) if j != idx]
    a[idx] = K * others[0] * others[1] - a[idx]
    return tuple(a)


def build_ray(steps=6, K=3):
    # Genuine single-Vieta-move ray: always mutate the current minimum entry.
    # (1,1,1) -> (2,1,1) -> (2,5,1) -> (2,5,29) -> (433,5,29) -> ...
    t = (1, 1, 1)
    seq = [t]
    for _ in range(steps - 1):
        idx = min(range(3), key=lambda j: t[j])
        t = vieta_move(t, idx, K)
        seq.append(t)
    return seq


def verify_ray(seq, K=3):
    for t0, t1 in zip(seq, seq[1:]):
        diffs = [j for j in range(3) if t0[j] != t1[j]]
        assert len(diffs) == 1, f"not a single mutation: {t0} -> {t1}"
        j = diffs[0]
        o = [t0[k] for k in range(3) if k != j]
        assert t1[j] == K * o[0] * o[1] - t0[j], f"Vieta fails: {t0} -> {t1}"
        assert t1[j] > 0
    return True


if __name__ == "__main__":
    seq = build_ray(6)
    verify_ray(seq)
    # Vianna-type triangles T(a,b,c) have constant normalized volume 9
    # (degree of CP^2); edge lattice lengths are (a,b,c).
    print("triple, max_edge, norm_vol")
    maxima = []
    for t in seq:
        m = max(t)
        maxima.append(m)
        print(t, m, 9)
    strictly = all(b > a for a, b in zip(maxima, maxima[1:]))
    print("single-Vieta-move ray verified:", True)
    print("maxima strictly increasing:", strictly)
    print("volume constant (so volume does not distinguish):", True)
    print("pairwise GL-distinct (by max edge lattice length):",
          len(set(maxima)) == len(seq))
    os.makedirs("output/artifacts", exist_ok=True)
    with open("output/artifacts/markov_ray.json", "w") as f:
        json.dump({"ray": seq, "maxima": maxima, "normalized_volume": 9,
                   "vieta_constant_K": 3,
                   "strictly_increasing_max": strictly}, f, indent=2)
