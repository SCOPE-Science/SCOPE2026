# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Thin Signorini isolated-conical quadratic stratum dimension
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1188
- **Disposition:** AUDIT_1_REJECT
- **Domain:** thin Signorini obstacle problem
- **Method:** Almgren frequency plus blow-up link regularity and dimension reduction

## Problem

Prove or disprove that for the thin Signorini obstacle problem in dimension n>=5, the isolated-conical quadratic singular stratum has Hausdorff dimension at most n-4. Objects: B1 in R^n with thin space H={x_n=0}; u in H^1(B1) with u>=0 on H, Delta u=0 in B1 minus the coincidence set on H, Delta u<=0 distributionally, even reflection and Almgren frequency N_{x0}(r) with limit kappa(x0)>=3/2 at free-boundary points x0 in H. Assumptions: kappa(x0)=2 and every subsequential blow-up u_{x0,r}(x)=u(x0+rx)/r^2 converges (subsequentially, weakly H^1 and locally uniformly) to a 2-homogeneous global minimizer u0 whose contact cone Lambda={u0=0} intersect H is a cone with vertex x0 such that (Lambda minus {x0}) is a C^2 embedded conical hypersurface in H, i.e. its link Lambda intersect S^{n-2} is a closed C^2 hypersurface with no further singularity (isolated conical). Let S_iso(u) be the set of such x0. Requested conclusion: dim_H S_iso(u)<=n-4 for every admissible u. Scope: all n>=5 and all admissible u with bounded H^1 norm. A complete answer is either a proof of the bound for all such u, or an explicit admissible u plus a Borel set E subset S_iso(u) with H^{n-3}(E)>0 (hence dim_H>=n-3) together with verification via Almgren limits and link regularity that each point of E has frequency 2 and only isolated-conical 2-homogeneous blow-ups.

## Attempted claim

Prove or disprove that for the thin Signorini obstacle problem in dimension n>=5, the isolated-conical quadratic singular stratum has Hausdorff dimension at most n-4. Objects: B1 in R^n with thin space H={x_n=0}; u in H^1(B1) with u>=0 on H, Delta u=0 in B1 minus the coincidence set on H, Delta u<=0 distributionally, even reflection and Almgren frequency N_{x0}(r) with limit kappa(x0)>=3/2 at free-boundary points x0 in H. Assumptions: kappa(x0)=2 and every subsequential blow-up u_{x0,r}(x)=u(x0+rx)/r^2 converges (subsequentially, weakly H^1 and locally uniformly) to a 2-homogeneous global minimizer u0 whose contact cone Lambda={u0=0} intersect H is a cone with vertex x0 such that (Lambda minus {x0}) is a C^2 embedded conical hypersurface in H, i.e. its link Lambda intersect S^{n-2} is a closed C^2 hypersurface with no further singularity (isolated conical). Let S_iso(u) be the set of such x0. Requested conclusion: dim_H S_iso(u)<=n-4 for every admissible u. Scope: all n>=5 and all admissible u with bounded H^1 norm. A complete answer is either a proof of the bound for all such u, or an explicit admissible u plus a Borel set E subset S_iso(u) with H^{n-3}(E)>0 (hence dim_H>=n-3) together with verification via Almgren limits and link regularity that each point of E has frequency 2 and only isolated-conical 2-homogeneous blow-ups.

## Research outcome

Disproved the n-4 Hausdorff bound: u=x1^2-xn^2 is admissible with an (n-2)-dimensional isolated-conical frequency-2 stratum, so H^{n-3}(E)=infinity.

## Why this attempt failed

Failed axes: originality, value.

originality: The headline disproof is mechanically implied by long-standing prior classification and is a renamed repackaging: the flat quadratic u=x1^2-xn^2 is the canonical rank-one case of the ACS08 Theorem 3 classification p=sum a_i(x_i^2-x_{n+1}^2), a_i>=0, quoted verbatim in Fernandez-Real/Torres-Latorre Lemma 2.1(c) and Petrosyan lecture notes Sec 4.3. Garofalo-Petrosyan 0804.2508 defines singular points by vanishing (n-1)-density, proves frequency 2m and structural containment, and explicitly states the whole free boundary can be singular when u is harmonic symmetric touching zero obstacle. Under the topic's literal definition that counts the flat equator S^{n-3} as isolated-conical, the (n-2)-dimensional flat singular set is therefore a direct corollary/special case of that stronger known theory under synonymous notation (quadratic blow-up, flat solution, singular/degenerate point). No new object, boundary, or implication beyond the textbook example; a timestamp or failed literal-title search does not establish priority. value: TARGET-route negative resolution exposes an ADMISSION_DEFECT: as written the isolated-conical definition counts the smooth flat hyperplane (punctured plane smooth, equator link closed hypersurface) so S_iso contains the classical flat stratum whose (n-2)-dimensionality is textbook. The claimed n-4 bound is then trivially false on the first canonical example any expert would try, i.e. a type/normalization over-inclusion, vacuity, cheap small-instance mismatch and direct lookup. Per TARGET policy such a negative resolution fails value even though literally false, and per STANDARD it is a textbook restatement / mere parameter substitution / known-database recomputation with no new boundary, motivation, or downstream use. ADMISSION_DEFECT: admission should have excluded flat links or ruled out this cheap defect; the untouched genuinely-curved stratum question remains open. Certification and exact algebra do not create value.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The disproof addresses exactly the stated isolated-conical definition, under which the flat hyperplane profile with equator link qualifies; if the intended class meant to exclude flat links, the bound for the remaining genuinely-curved stratum is untouched and would require separate analysis. No regularity beyond the explicit polynomial is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
