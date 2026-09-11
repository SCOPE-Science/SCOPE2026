# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified transverse Kakeya-bush extremizer saturating the three-cap cell estimate

## 1. Statement

Let P = {(xi, |xi|^2)} in R^3 with extension
(Ef)(x) = int e^{i(x' . xi + x_3 |xi|^2)} f(xi) dxi.
Fix R = 2^10 = 1024, s = R^{-1/2} = 1/32, a = s/2 = 1/64, and three caps

  Q_1 = (-a,a]^2,  Q_2 = (1/2,0)+(-a,a]^2,  Q_3 = (0,1/2)+(-a,a]^2,

each an R^{-1/2}-cap inside the unit disc (far-corner modulus <= 0.516).
Put f_k = 1_{Q_k} (0/1 data). Partition each Q_k into a 32 x 32 grid of disjoint
tiles of side delta = s/32 = R^{-1} = 1/1024; there are exactly R = 1024 packets
per cap, 3072 in all, all with coefficient 1.

**Theorem.** At R = 2^10:
(i) the three caps are transverse: |det| of the three central unit normals is
exactly 1/2, and the minimum |det| over all 64 corner triples is >= 0.45;
(ii) the R packets per cap form a plate-bush: each packet's dual tube
(R^{1/2} x R^{1/2} x R, radius 32) is aimed through the origin, so all 3072 =
3R tubes meet B_{R^{1/2}}(0) with per-cap multiplicity 1024 = R (c = 1);
(iii) the trilinear ratio

  L := ||(prod_{k=1}^3 |E f_k|)^{1/3}||_{L^6(B_R)} / prod_{k=1}^3 ||f_k||_2^{1/3}

satisfies L >= 0.112 while the universal pointwise envelope gives L <= 1.28,
hence with U = 1.28 any finite cell upper bound at this scale is matched up to
factor <= 12, i.e. L >= (log R)^{-2} U with c_1 = 1, C_1 = 2 in either log base
(in fact L >= 4 (ln R)^{-2} U and L >= 8 (log_2 R)^{-2} U).
So the partitioning cell step is sharp at this scale up to the claimed log power.

## 2. Tube dictionary and overlap count

For tile (k,i,j) with center eta in Q_k, the assigned dual tube has axis direction
equal to the paraboloid unit normal (-2eta,1)/|(-2eta,1)|, radius R^{1/2} = 32,
half-length 512 (full length ~R), and central line through the origin; direction
duality is exact at the tile center (angle 0), and every tile center lies within
s/sqrt(2) of its cap center, so each tube is dual to its cap up to O(R^{-1/2}).
The tile normals fan out across the cap by O(s); the R tubes per cap are distinct
tubes through the origin separating by O(R^{1/2}) at distance R. The full table
(3072 rows: cap, tile indices, tile center, unit direction, radius, origin
distance 0) is `artifacts/tube_table.csv`; the all-ones coefficient vector is
`artifacts/coefficients.csv`. Scope note: the tiles are disjoint sub-cap frequency
pieces (side R^{-1}), so per-tile spatial concentration inside the thin tube is
not claimed or needed; what is certified is (i) direction duality to the cap,
(ii) exact geometric overlap below, and (iii) the analytic L^6 bound of Section 3,
which uses only the full f_k = sum of its tiles. Since every assigned axis passes
through the origin, the overlap multiplicity at 0, hence in B_{32}(0), is
3072 = 3R, per cap R: overlap >= cR with c = 1 per cap. See
`artifacts/overlap_table.csv`.

## 3. L^6 ratio: rigorous lower bound

||f_k||_2^2 = s^2 = 2^{-10} each, so the denominator is D = s = 1/32.
Write Ef_k(x) = e^{iPhi_k(x)} int_{(-a,a]^2} e^{ipsi} du with
Phi_k(x) = x'.c_k + x_3|c_k|^2 and
psi = (x'+2x_3 c_k).u + x_3|u|^2, u in (-a,a]^2.
For x in B_rho with rho = 10: |x' + 2x_3 c_k| <= 10(1+2(1/2)) = 20,
|u| <= a sqrt(2), so |psi| <= 20 a sqrt(2) + 100 a^2 = 10(sqrt(2)/32 + 1/2048)
<= 0.449 (using sqrt(2) <= 1.42). Since cos is even and decreasing on [0,pi],
Re e^{ipsi} = cos psi >= cos(0.449) >= 1 - 0.449^2/2 >= 0.899, whence

  |Ef_k(x)| >= 0.899 s^2   for all x in B_10, all k.

Thus (prod|Ef_k|)^{1/3} >= 0.899 s^2 on B_10 and, with |B_10| = 4000 pi/3 >=
4000(3.14)/3 = 4186.7 >= 4096 = 4^6,

  ||(prod|Ef_k|)^{1/3}||_{L^6(B_R)} >= 0.899 s^2 |B_10|^{1/6} >= 0.899 s^2 * 4,

and dividing by D = s gives L >= 0.112. The script asserts each numeric step.

## 4. Envelope upper bound and log saturation

Pointwise |Ef_k| <= |Q_k| = s^2 gives
L <= s |B_R|^{1/6} <= ((4pi/3)R^3)^{1/6} s <= (4.2)^{1/6} <= 1.28 =: U
(using pi <= 3.15 and the asserted 1.28^6 = 4.398 >= 4.2).
Hence U/L <= 1.28/0.112 <= 11.43 <= 12.
With ln R = 6.9315, (ln R)^2 = 48.05 <= 49 (asserted) and log_2 R = 10:

  L >= 4 (ln R)^{-2} U,   L >= 8 (log_2 R)^{-2} U,

in particular L >= c_1 (log R)^{-C_1} U with c_1 = 1, C_1 = 2 in either base.
For scale: R^{-1/4} = 0.1768 and L/R^{-1/4} = 0.63, an order-one constant.

## 5. Reproducibility

Run `python3 artifacts/certify_target.py` (stdlib + numpy): it rechecks cap
containment, exact transversality 1/2, corner minimum 0.4507, the 3072-row
dictionary written to `tube_table.csv`, the 0/1 coefficients, the overlap table,
every numeric inequality above (via assert), and writes `certify_log.txt`,
`overlap_table.csv`, `ratio_certificate.csv`. A 400x400-per-tile quadrature
spot check (illustration only, not part of the proof) confirms |Ef_k| at 0 and
at (5,0,0), (0,5,5), (10,-3,7), (0,0,10) all exceed the 0.899 s^2 floor.

## 6. Scope and limits

Proved: finite-scale (R = 2^10) transverse 3-cap bush with counted overlap 3R
and trilinear L^6 ratio pinned in [0.112, 1.28], saturating any cell estimate
at this scale within (log R)^2. Not proved: asymptotics as R -> oo, sharpness
of the log power 2, or anything about the wall term; the upper side is the
trivial envelope, so "cell estimate" here means any finite bound at this scale.
Originality: transverse, counted, cap-anchored 3-cap witness per the admission
gap; generic Knapp/transverse examples (Demeter Ch.10) and multilinear Kakeya
geometry (Guth; Bennett-Carbery-Tao) do not record it.
