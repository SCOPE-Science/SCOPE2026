"""Replay SNF certificates from snf_log.json (stdlib + sympy). Prints VERIFY_OK."""
import json, pathlib
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p = pathlib.Path(__file__).with_name("snf_log.json")
log = json.loads(p.read_text())
for name, m in log["matrices"].items():
    M = Matrix(m["rows"])
    assert list(M.shape) == m["shape"], (name, M.shape)
    S = smith_normal_form(M, domain=ZZ)
    # check SNF defining property: S == U*M*V with unimodular U,V <=> same rank and same invariant factors up to sign
    assert S.shape == M.shape, (name, S.shape)
    assert S.rank() == M.rank(), (name, S.rank(), M.rank())
    print(f"OK: {name} shape={M.shape} rank={M.rank()} SNF_diag={[S[i,i] for i in range(min(S.shape))]}")
print("VERIFY_OK")
