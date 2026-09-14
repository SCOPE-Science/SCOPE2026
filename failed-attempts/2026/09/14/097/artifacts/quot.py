"""Quotient algebra A=S/I data: graded bases, projectors, multiplication. Exact QQ."""
import sys; sys.path.insert(0, 'output/artifacts')
from fractions import Fraction
from apolar import mons
import sympy as sp

class QA:
    def __init__(self, mingens, nvars=4, dmax=None):
        self.mingens = [(d, {e: Fraction(c) for e, c in p.items()}) for d, p in mingens]
        self.n = nvars
        soc = max((d for d, _ in mingens), default=0)
        self.dmax = dmax if dmax is not None else soc + 1
        self.ms = {}     # deg -> monomial list
        self.free = {}   # deg -> list of monomial exps (basis)
        self.P = {}      # deg -> projector matrix (dimQ x nmon), QQ
        self.dim = {}
        for j in range(self.dmax + 1):
            ms = mons(nvars, j)
            self.ms[j] = ms
            rows = []
            for dg, g in self.mingens:
                if dg > j: continue
                for m in mons(nvars, j - dg):
                    row = [Fraction(0)] * len(ms)
                    for e, c in g.items():
                        ne = tuple(a + b for a, b in zip(e, m))
                        row[ms.index(ne)] += c
                    rows.append(row)
            if rows:
                M = sp.Matrix(rows)
                R, piv = M.rref()
                piv = list(piv)
                F = [k for k in range(len(ms)) if k not in piv]
                # projector: coord on F: v |-> v[F] - sum_i v[P_i]*R[i,F]
                Pmat = sp.zeros(len(F), len(ms))
                for q, k in enumerate(F):
                    Pmat[q, k] = 1
                for i, pi in enumerate(piv):
                    for q, k in enumerate(F):
                        Pmat[q, pi] -= R[i, k]
            else:
                F = list(range(len(ms)))
                Pmat = sp.eye(len(ms))
            self.free[j] = [ms[k] for k in F]
            self.P[j] = Pmat
            self.dim[j] = len(F)
        self.socle = max((j for j in range(self.dmax + 1) if self.dim[j] > 0), default=0)

    def mul(self, w, j):
        """Matrix (dim_{j+1} x dim_j): multiplication by variable w on A_j -> A_{j+1}."""
        if j + 1 > self.dmax or self.dim[j] == 0: return sp.zeros(self.dim.get(j + 1, 0), self.dim[j])
        msj1 = self.ms[j + 1]
        M = sp.zeros(len(msj1), self.dim[j])
        for c, m in enumerate(self.free[j]):
            ne = list(m); ne[w] += 1; ne = tuple(ne)
            M[msj1.index(ne), c] = 1
        return self.P[j + 1] * M

    def _build(self, j):
        ms = mons(self.n, j)
        self.ms[j] = ms
        rows = []
        for dg, g in self.mingens:
            if dg > j: continue
            for m in mons(self.n, j - dg):
                row = [Fraction(0)] * len(ms)
                for e, c in g.items():
                    ne = tuple(a + b for a, b in zip(e, m))
                    row[ms.index(ne)] += c
                rows.append(row)
        if rows:
            M = sp.Matrix(rows)
            R, piv = M.rref()
            piv = list(piv)
            F = [k for k in range(len(ms)) if k not in piv]
            Pmat = sp.zeros(len(F), len(ms))
            for q, k in enumerate(F):
                Pmat[q, k] = 1
            for i, pi in enumerate(piv):
                for q, k in enumerate(F):
                    Pmat[q, pi] -= R[i, k]
        else:
            F = list(range(len(ms)))
            Pmat = sp.eye(len(ms))
        self.free[j] = [ms[k] for k in F]
        self.P[j] = Pmat
        self.dim[j] = len(F)

    def _ensure(self, j):
        if j not in self.ms:
            self._build(j)

    def proj(self, poly, j):
        """Project poly dict (degree j) to coordinate vector on A_j basis."""
        if j < 0:
            return sp.zeros(0, 1)
        self._ensure(j)
        ms = self.ms[j]
        v = sp.Matrix([poly.get(e, Fraction(0)) for e in ms])
        return self.P[j] * v
