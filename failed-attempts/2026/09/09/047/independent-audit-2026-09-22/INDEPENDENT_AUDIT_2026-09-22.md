# Independent audit — 2026-09-26

Record: `2026/09/09/047`. Verdict: **correctness PASS (characteristic 2 point); originality PASS (explicit vector only); scientific value FAIL.** Disposition: archive full original package.

## Correctness
I independently expanded the 56 3×3 determinants as polynomials in F2[t]. Exactly the seven listed Fano triples vanish, 40 valuations are zero, six are one and three are two. Enumerating the record's 1,960 general tropical basis-exchange Plücker inequalities gives zero violations. The 280 disjoint three-term rank-3 relations follow from the same determinant realization. Thus the explicit w is a valued matroid and is realizable over characteristic 2 as a point of the tropical Grassmannian over an algebraic closure of F2((t)). The finite initial matroid has the claimed Fano deletion. The matrix proves existence of this *point*, not realizability of every vector in a Dressian cone; “cell” is read existentially here.

## Prior work and originality
Herrmann–Joswig–Speyer, arXiv:1112.1278, compute the Dr(3,8) fan and the general relation to tropical Grassmannians. Bendle–Böhm–Ren–Schröter, arXiv:2003.13752, explicitly study TGr_0(3,8), and their Section 4.6 relates nonrealizable characteristic-zero cones to Fano extensions. The particular F2[t] matrix and its 56-entry vector are a concrete new example within the materials compared, but valuation of actual minors automatically gives a lift; no cone or orbit is identified or classified.

## Scientific value
The advertised Dr-versus-TGr(3,8) boundary is the characteristic-zero problem of the cited comparison. This example has seven identically vanishing Fano minors, so its underlying matroid restricts to F7 and cannot be realized over characteristic zero. It therefore cannot certify membership in TGr_0(3,8), or overturn the cited 23 extended-Fano obstructions. Its single characteristic-two point is an elementary construction, with no cell-wide lifting statement, enumeration, or obstruction; the remaining scientific value for the stated problem is insufficient. The record should explicitly distinguish TGr_2 from TGr_0 and either identify a substantive characteristic-two question or give a characteristic-zero certificate.

Sources: original RESULT.md and artifacts/verify_dressian_cell.py; https://arxiv.org/html/1112.1278v3; https://arxiv.org/html/2003.13752v1.
