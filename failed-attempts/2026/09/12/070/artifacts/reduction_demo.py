"""Toy validation of the PlainSelfTargetMSIS -> SelfTargetMSIS programming reduction.

Small ring R_q = Z_q[X]/(X^n+1), n=8, q=257, k=l=2, tau=3.
Mirrors the proof in output/DRAFT.md:
  - Plain solver P(A) -> (w, c, z) with A z = c w, c in B_tau, 0<||z||<=zeta.
  - Reduction S(A): runs P on the SAME matrix (identity-coupling resample),
    simulates P's oracle queries privately, samples a fresh M*, issues ONE
    program query H[(w,M*)] := c on the real oracle, outputs (w,M*,c,z).
  - Verifier checks H[(w,M)] == c, A z == c w, norm bound, z != 0.
Also tests a "locking" Plain-solver variant that reads the (simulated) hash
before outputting: the reduction still converts it because the programmed
point uses a fresh M* never visible to P.
Writes output/artifacts/results.json.
"""
import json
import os
import random

N = 8
Q = 257
K = L = 2
TAU = 3
ZETA = 8
TRIALS = 200

random.seed(1235)


def centered(x):
    x %= Q
    return x - Q if x > Q // 2 else x


def padd(a, b):
    return [(x + y) % Q for x, y in zip(a, b)]


def pmul(a, b):
    tmp = [0] * (2 * N)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            tmp[i + j] = (tmp[i + j] + x * y) % Q
    for i in range(N, 2 * N):
        tmp[i - N] = (tmp[i - N] - tmp[i]) % Q
    return tmp[:N]


def pnorm_inf(a):
    return max(abs(centered(x)) for x in a)


def mat_vec_mul(A, v):
    out = []
    for row in A:
        acc = [0] * N
        for a, x in zip(row, v):
            acc = padd(acc, pmul(a, x))
        out.append(acc)
    return out


def mat_eq(U, V):
    return all((x - y) % Q == 0 for u, v in zip(U, V) for x, y in zip(u, v))


def scalar_mul_vec(c, v):
    return [pmul(c, x) for x in v]


def rand_poly():
    return [random.randrange(Q) for _ in range(N)]


def rand_short_poly():
    return [random.choice([-1, 0, 1]) % Q for _ in range(N)]


def fixed_challenge():
    c = [0] * N
    for i in (0, 3, 5):
        c[i] = 1
    return c  # tau=3 sparse ternary element of B_tau


C0 = fixed_challenge()


def rand_matrix():
    return [[rand_poly() for _ in range(L)] for _ in range(K)]


class Oracle:
    """Lazy RO with values in B_tau; supports one-shot programming."""

    def __init__(self):
        self.table = {}
        self.programs = 0
        self.queries = 0

    def query(self, pt):
        self.queries += 1
        if pt not in self.table:
            c = [0] * N
            for i in random.sample(range(N), TAU):
                c[i] = random.choice([1, Q - 1])
            self.table[pt] = c
        return self.table[pt]

    def program(self, pt, c):
        assert pt not in self.table, "program point already defined!"
        self.table[pt] = list(c)
        self.programs += 1


def key(pt):
    w, m = pt
    return (tuple(tuple(p) for p in w), m)


def plain_solver(A, sim_oracle, locking=False):
    """Trivial Plain win (w unconstrained): u short, w = A u, z = c0 u."""
    for _ in range(100):
        u = [rand_short_poly() for _ in range(L)]
        z = scalar_mul_vec(C0, u)
        if any(any(v != 0 for v in x) for x in z):
            break
    w = mat_vec_mul(A, u)
    if locking:  # reads the hash first (on the SIMULATED oracle only)
        sim_oracle.query(key((w, "m0")))
        sim_oracle.query(key((w, "m1")))
    return w, list(C0), z


def verify_self(A, real_oracle_table, w, m, c, z):
    if key((w, m)) not in real_oracle_table:
        return False, "hash point undefined"
    if real_oracle_table[key((w, m))] != c:
        return False, "hash mismatch"
    if not mat_eq(mat_vec_mul(A, z), scalar_mul_vec(c, w)):
        return False, "equation fails"
    if all(all(v == 0 for v in x) for x in z):
        return False, "z == 0"
    if max(pnorm_inf(x) for x in z) > ZETA:
        return False, "norm exceeds zeta"
    if sum(1 for v in c if v in (1, Q - 1)) != TAU:
        return False, "challenge not in B_tau"
    return True, "ok"


def reduction_run(A, real_oracle, locking):
    sim = Oracle()  # private simulation; real oracle untouched until program
    w, c, z = plain_solver(A, sim, locking=locking)
    assert sim.queries >= 0
    for _ in range(1000):
        m_star = "msg-%032x" % random.getrandbits(128)
        if key((w, m_star)) not in real_oracle.table:
            break
    real_oracle.program(key((w, m_star)), c)  # the single allowed reprogram
    return w, m_star, c, z


def main():
    out = {"params": {"n": N, "q": Q, "k": K, "l": L, "tau": TAU,
                      "zeta": ZETA, "trials": TRIALS}}
    for locking in (False, True):
        plain_wins = self_wins = 0
        max_norm = 0
        progs = []
        for _ in range(TRIALS):
            A = rand_matrix()
            real = Oracle()
            w, m, c, z = reduction_run(A, real, locking=locking)
            # plain predicate check
            if (mat_eq(mat_vec_mul(A, z), scalar_mul_vec(c, w))
                    and any(any(v != 0 for v in x) for x in z)
                    and max(pnorm_inf(x) for x in z) <= ZETA):
                plain_wins += 1
            ok, _ = verify_self(A, real.table, w, m, c, z)
            self_wins += ok
            max_norm = max(max_norm, max(pnorm_inf(x) for x in z))
            progs.append(real.programs)
        out["locking=%s" % locking] = {
            "plain_win_rate": plain_wins / TRIALS,
            "self_win_rate": self_wins / TRIALS,
            "programs_per_run": sum(progs) / len(progs),
            "max_observed_norm": max_norm,
            "zeta_preserved": max_norm <= ZETA,
        }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "results.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
