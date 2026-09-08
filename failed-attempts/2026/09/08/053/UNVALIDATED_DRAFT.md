# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact minimal faithful permutation degrees for a 29-group benchmark family of 2-groups (orders 32 and 64)

## 1. Definitions

For a finite group $G$, the **minimal faithful permutation degree** $\mu(G)$
is the least $n$ with $G \hookrightarrow S_n$. Equivalently (Johnson),
$\mu(G)$ is the least index sum $\sum_i [G{\colon}H_i]$ over subgroup families
with **trivial core intersection** $\bigcap_i \mathrm{Core}_G(H_i) = 1$, where
$\mathrm{Core}_G(H) = \bigcap_{g \in G} gHg^{-1}$.
Indeed, the kernel of the disjoint-union coset action on
$\bigsqcup_i G/H_i$ equals $\bigcap_i \mathrm{Core}_G(H_i)$, so the action is
faithful iff the core intersection is trivial, and its degree is the index sum.

## 2. Theorem (partial; exactly as certified)

Let $\mathcal{F}_{32}$ (15 groups) and $\mathcal{F}_{64}$ (14 groups) be the
explicitly realized 2-groups below. Then every $\mu(G)$ value in the following
table is exact, each with a stored minimizing witness family whose core
intersection is trivial:

**Order 32.** C32: 32 [32]; C16xC2: 18 [2,16]; C8xC4: 12 [4,8];
C8xC2xC2: 12 [4,8]; C4xC4xC2: 10 [2,4,4]; C4xC2^3: 10 [2,4,4]; C2^5: 10 [2,4,4];
D32: 16 [16]; SD32: 16 [16]; Q32: 32 [32]; D16xC2: 10 [2,8]; Q16xC2: 18 [2,16];
D8xC2xC2: 8 [4,4]; Eplus32 (D8*D8): 8 [8]; Eminus32 (D8*Q8): 16 [16].

**Order 64.** C64: 64 [64]; C32xC2: 34 [2,32]; C16xC4: 20 [4,16];
C8xC8: 16 [8,8]; C4^3: 12 [4,4,4]; C4xC4xC2xC2: 12 [4,4,4]; C2^6: 12 [4,4,4];
D64: 32 [32]; SD64: 32 [32]; Q64: 64 [64]; D32xC2: 18 [2,16];
D16xC4: 12 [4,8]; Q32xC2: 34 [2,32]; Eplus32xC2: 10 [2,8].

**Corollaries (within the surveyed family only).**
(a) The order-32 maximum is $\mu=32$, attained exactly by C32 and Q32; the next
distinct value is 18, giving an integer gap of 14.
(b) The order-64 maximum is $\mu=64$, attained exactly by C64 and Q64; the next
distinct value is 34, giving an integer gap of 30.

Group realizations: abelian types as direct products of cyclics; D/SD/Q families
via $(a,b)=r^as^b$, $srs^{-1}=r^u$, $s^2=r^{s2}$ with $u^2=1$, $us2=s2$
(dihedral $u=-1,s2=0$; semidihedral $u=2^{k-1}-1,s2=0$; quaternion $u=-1$,
$s2=2^{k-1}$); direct products as componentwise tables; extraspecials as central
products $(D8\times D8)/\langle(z,z)\rangle$ and $(D8\times Q8)/\langle(z,z)\rangle$.
Axioms were checked exhaustively on every Cayley table.

## 3. Proof / certification method

1. **Subgroups:** complete adjunction-closure DFS from $\{1\}$; every subgroup
   is reached by adjoining its elements one at a time.
2. **Cores:** brute-force intersection of all conjugates.
3. **Upper bound:** minimizing family stored per group (generator tuples,
   masks, cores, indices); core intersection verified $=1$, so the coset action
   is faithful of degree $\mu$.
4. **Lower bound (minimality):** for each core value keep the cheapest index;
   exact Dijkstra shortest path over the normal-subgroup intersection lattice
   from $G$ to $1$. Any faithful family yields a path of equal cost and vice
   versa, so the distance is exactly $\mu(G)$.
5. **Independent replay:** `verify.py` (separately written code) re-derives group
   axioms, subgroup counts, witness subgroup/core data, faithfulness, Dijkstra
   optima, maxima/gaps, and the abelian Johnson cross-checks (14/14 match).
   Result: ALL 29 GROUPS VERIFIED.

## 4. Reproduction

```
python3 output/artifacts/compute_mu.py   # rebuilds mu_results.json
python3 output/artifacts/verify.py       # independent verification
```
Stdlib only (itertools, json, heapq); ran in minutes on one core.

## 5. Scope limits (explicit)

This is a **benchmark fragment, not the full 51+267 SmallGroups census**:
the lane had no GAP/SmallGroups library, so the fallback's full-window table
could not be honestly completed. No SmallGroups IDs are claimed; groups are
identified by committed presentations/Cayley tables. Maxima and gaps are
asserted only within the surveyed 29-group family. The reusable stdlib audit
pipeline (Cayley table -> subgroups -> cores -> Dijkstra optimum -> replay) is
the delivered reusable component.

## 6. Relation to prior work

O'Brien–Prajapati–Udeep (arXiv:2306.11337) determines $\mu$ for order $p^6$,
$p$ odd, explicitly excluding $p=2$; cyclic-center formulas
(arXiv:2302.06257), Coxeter/binary-polyhedral values (arXiv:0812.0182), and
Fitting-free complexity (arXiv:2501.16039) imply no value in this window.
No prior source records this exact 29-row certified table with witness families.
