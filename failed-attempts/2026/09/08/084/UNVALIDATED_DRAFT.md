# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact ECH capacities c_1..c_8 for 268 rational concave toric domains of height <= 6, with a certified beyond-volume-and-width embedding obstruction

## Claim

Let C_6 be the set of integral concave toric domains X_Omega in C^2 whose
moment chain is (a,0)=Q_0,Q_1,...,Q_n=(0,b) with 1<=a,b<=6, at most two
interior kinks, strictly convex upper graph (slopes strictly increasing).
|C_6| = 268. For every X in C_6 we compute exactly c_0..c_8(X) (c_0=0) by the
concave lattice-path formula (Theorem 1.21 of Choi-Cristofaro-Gardiner-
Frenkel-Hutchings-Ramos, arXiv:1310.6647):

  c_k(X_Omega) = max{ ell_Omega(Lambda) : L(Lambda) = k }

over concave integral paths Lambda, with L = enclosed lattice count (off-path)
and ell_Omega the support action. Full table: `artifacts/c6_table.json`
(sha256 `1a202fce...adbcc603b`, see `artifacts/table_sha256.txt`).

Witness pair (both in C_6, Hutchings weight sequences verified by the volume
identity sum a_i^2/2 = area):

  X* = chain ((4,0),(2,1),(0,2)), weights (2,2), vol 4,
       c_1..c_8 = 2,4,4,6,6,8,8,8;
  Y* = chain ((4,0),(1,1),(0,6)), weights (2,1,1,1,1,1,1), vol 5,
       c_1..c_8 = 2,3,4,5,6,7,8,9.

Hence there is NO symplectic embedding int(X*) -> Y*: c_2(X*)=4 > 3=c_2(Y*)
(ECH monotonicity, Hutchings 1005.2260). The obstruction is strict beyond both
classical constraints: vol(X*)=4 < 5=vol(Y*) (volume silent) and
c_1(X*)=2=c_1(Y*) (Gromov width silent); the ratio c_2(X*)/c_2(Y*) = 4/3.
Capacities agree byte-for-byte between the lattice-path computation and the
independent Hutchings weight-sequence + disjoint-union DP computation
(Theorem 1.4 of 1310.6647) for both witness domains.

## Evidence (reproducible, exact rational arithmetic)

1. Lattice-path engine (`artifacts/lattice_ech.py`): exhaustive enumeration of
   all 65 concave integral paths with L<=8 (finitely many for fixed k: Lemma 2.4
   of 1310.6647); per-domain maximization of ell_Omega with argmax path logged
   (`artifacts/witness_certificate.json`, per-k argmax + path counts).
2. Calibration: reproduces c(B(1)) = 1,1,2,2,2,3,3,3 and
   c(E(2,1)) = 1,2,2,3,3,4,4,4 (Ellipsoid property N(a,b)).
3. Independent replay: L crosschecked by Pick's theorem (0/65 mismatches);
   ell crosschecked by a second support implementation on all 268 domains
   (0 mismatches); weight-DP capacities agree with lattice capacities on both
   witness domains (9/9 each).
4. Witness detail (k=2): X* argmax path [(0,1),(2,0)], edge v=(2,-1),
   min over graph {(4,0),(2,1),(0,2)} of v-cross = min(4,4,4) = 4.
   Y* maximum 3: same path gives min over {(4,0),(1,1),(0,6)} = min(4,3,12) = 3,
   and no L=2 path scores higher (exhaustive: 2 paths with L=2).
5. Weight verification: X* weights (2,2): 8/2=4=area; Y* weights
   (2,1x6): (4+6)/2=5=area; DP argmax partitions logged in code.

## What is NOT claimed

- No sharpness claim (no optimal-embedding assertion); no stabilized (x C^N)
  claim: the obstruction is a plain 4-dimensional ECH monotonicity obstruction.
  The topic's "stabilized" headline is therefore only partially met; we claim
  the fallback exact-table + strict-obstruction result (admission fallback).
- Weight sequences are certified (volume identity + capacity agreement) for 129
  domains including the witness pair; the remaining 139 table entries rest on
  the lattice-path formula alone (weight recursion hits the isolated-cut-lens
  case there; see Limitations).
- C_6 covers integral chains with <=2 kinks (268 domains), a finite,
  explicitly committed stratum of "height <= 6" (intercepts <= 6); rational
  non-integral vertices are not enumerated (approximation by continuity only).

## Limitations / uncertainty

- The Choi et al. weight recursion (Sec 1.3) in the form "line meets graph in a
  segment" does not directly cover cuts meeting the graph in >=2 isolated
  points (a frequent integer-chain case, e.g. ((3,0),(2,2),(0,3)) with
  w=3=a=b); our chain recursion drops the middle lens there and fails the
  volume identity on 139/268 domains. Those domains' capacities are certified
  only via the lattice-path theorem (Thm 1.21), which is uniform and was the
  primary engine; a full packing-based weight list for them would need the
  lens-piece extension.
- Originality: general formulas are prior art (Hutchings; Choi et al.;
  McDuff-Schlenk); novelty is the exhaustive exact c_1..c_8 census over this
  committed 268-domain stratum plus the specific certified obstruction pair,
  per admission review (no live source publishes it).
- All computations are exact (Fractions / integer Pick); no floating point in
  the certificate path.

## Reproduce

  cd output && python3 -c "
  import json
  from artifacts.lattice_ech import concave_paths_for_k, omega_length
  from artifacts.weight_ech import disjoint_union_caps
  from artifacts.fastw import concave_weights
  rows = json.load(open('artifacts/c6_table.json')); paths = concave_paths_for_k(8)
  X=[(4,0),(2,1),(0,2)]; Y=[(4,0),(1,1),(0,6)]
  for ch in [X,Y]:
      lat=[max(omega_length(v,ch) for v,L in paths if L==j) for j in range(9)]
      dp,_=disjoint_union_caps(concave_weights(ch),8)
      assert [str(x) for x in lat]==rows[str(tuple(ch))]==[str(x) for x in dp]
  print('witness replay OK: c2 = 4 > 3, vols 4 < 5')"
