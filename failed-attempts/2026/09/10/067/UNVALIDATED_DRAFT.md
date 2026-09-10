# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# The stated d3-inequality for the cork pullback pair is impossible

## Statement proved

Let $W$ be any compact contractible oriented smooth $4$-manifold with
$Y=\partial W$ (in particular any fixed Mazur-type cork $W^*$), and let
$\tau\colon Y\to Y$ be any orientation-preserving diffeomorphism
(in particular any cork boundary involution).
Let $\xi_0$ be any contact structure on $Y$ and put
$\xi_1=\tau_*\xi_0$ (the boundary pushforward reading of "$J_1=\tau^*J_0$").
Then both $d_3(\xi_0)$ and $d_3(\xi_1)$ are defined in $\mathbb{Q}$ and

$$d_3(\xi_1)=d_3(\xi_0).$$

**Corollary.** The lane-662 target claim — which asserts, for such a pair,
$d_3(\xi_1)\ne d_3(\xi_0)$ **and** $c^+(\xi_0)\ne c^+(\xi_1)$ — is false as
stated, for *every* choice of diagram $D^*$, Stein structure $J_0$, and
cork involution $\tau$. The conjunction fails at the first conjunct
regardless of the truth value of the $c^+$ conjunct. This is a complete
TARGET resolution by rigorous disproof. No claim is made about the
$c^+$-comparison alone.

## Proof

### Step 1. $Y$ is an integral homology sphere; $d_3$ is defined.

$W$ contractible gives $H_1(W)=H_2(W)=0$. The long exact sequence of the
pair $(W,Y)$ contains

$$H_2(W)\to H_2(W,Y)\to H_1(Y)\to H_1(W),$$

i.e. $0\to H_2(W,Y)\to H_1(Y)\to 0$, so $H_1(Y)\cong H_2(W,Y)$.
By Poincar\'e–Lefschetz, $H_2(W,Y;\mathbb{Z})\cong H^2(W;\mathbb{Z})=0$.
Hence $H_1(Y)=0$: $Y$ is a closed connected oriented $3$-manifold with
$H_1=0$, i.e. an integral homology sphere. Then $H^2(Y;\mathbb{Z})=0$, so
$c_1(\xi)$ is (trivially) torsion for every plane field $\xi$, and Gompf's
$d_3\in\mathbb{Q}$ is defined on all of them.

### Step 2. $\tau$ is orientation-preserving.

By definition a cork involution $\tau$ on $Y=\partial W$ extends to an
orientation-preserving homeomorphism $F\colon W\to W$ (indeed this is what
makes the cork twist produce a homeomorphic-but-nondiffeomorphic pair).
The Stokes-induced boundary orientation is natural under orientation-
preserving maps of pairs, so $\tau=F|_Y$ is orientation-preserving as a
diffeomorphism of the oriented $3$-manifold $Y$. Concretely, in the
standard symmetric Kirby picture (dot/zero exchange) $\tau$ is visibly a
rotation, of local degree $+1$.

### Step 3. Naturality of $d_3$.

Gompf's $d_3$ classifies, for fixed torsion Spin$^C$ data, the homotopy
class of the oriented $2$-plane field over the $2$-skeleton relative data;
it can be computed from any almost-complex filling $(X,J)$ with
$\partial(X,J)=(Y,\xi)$ and no $+1$ surgeries by

$$d_3(\xi)=\frac{c_1^2(X,J)-3\sigma(X)-2\chi(X)}{4}+q(X),$$

(Gompf, *Handlebody construction of Stein surfaces*, Ann. of Math. 1998;
see also Ding–Geiges–Stipsicz survey). Every ingredient —
$\chi$, $\sigma$, $c_1^2$ (with $c_1$ pushed forward), $q$ — is preserved
under an orientation-preserving diffeomorphism $\phi\colon Y\to Y$
transporting the plane field and its fillings. Equivalently, $\phi_*$
induces a homotopy-class-preserving bijection on plane fields with the
same Spin$^C$ data. Hence for every orientation-preserving $\phi$ and
every $\xi$ with torsion $c_1$,

$$d_3(\phi_*\xi)=d_3(\xi).$$

### Step 4. Conclusion.

Apply Step 3 with $\phi=\tau$, $\xi=\xi_0$: $d_3(\xi_1)=d_3(\xi_0)$
identically. The target's required strict inequality
$d_3(\xi_1)\ne d_3(\xi_0)$ is therefore unsatisfiable for every
$W^*/D^*/J_0/\tau$. Since the target is a conjunction containing this
conjunct, the target is false. ∎

## Remarks on scope (what is and is not shown)

1. **Interior pullback is ill-posed.** As stated, "$J_1=\tau^*J_0$" pulls
   back by a map defined only on the boundary $Y$, so $J_1$ is not defined
   as a Stein structure on the interior of $W^*$. The proof above grants
   the most charitable boundary reading $\xi_1=\tau_*\xi_0$ and still
   refutes the $d_3$ inequality.
2. **$c^+$ untouched.** The proof says nothing about whether
   $c^+(\xi_0)\ne c^+(\xi_1)$ could hold, nor whether $\tau$ extends as a
   contactomorphism, nor whether $J_0,J_1$ are homotopic as Stein
   structures. Those remain open; only the *conjoined* target (which
   demands the $d_3$ gap) is disproved.
3. **Correct repair direction.** Any future boundary-detector for
   $\tau^*\!J_0$-type pairs must use invariants that are *not* natural
   under pushforward in this way, or must compare fillings that are not
   related by pushforward (e.g. genuinely distinct Stein structures on a
   fixed $W$, as in Karakurt–Oba–Ukida's admissible-vs-planar pair, not a
   $\tau$-pullback pair). The $d_3$-gap route for a pullback pair is
   closed.

## Verification

`output/artifacts/verify_target.py` (stdlib only) replays:
- $H_1(Y)=0$ forcing via the pair LES + Poincar\'e–Lefschetz ranks;
- Gompf-value invariance under transport of filling data on sample
  $(c^2,\sigma,\chi)$ tuples;
- boolean unsatisfiability of $(d_1\ne d_0)\land B$ given forced $d_1=d_0$.

Run: `python3 output/artifacts/verify_target.py` → `VERIFY_OK`.

## References (method only; no prior art implies the target)

- R. Gompf, Handlebody construction of Stein surfaces, Ann. of Math. 148
  (1998), 619–693 (Stein $tb-1$ criterion; $d_3$ formula).
- F. Ding, H. Geiges, A. Stipsicz, Surgery diagrams for contact
  3-manifolds, Turkish J. Math. 28 (2004) ($d_3$ naturality survey).
- O. Plamenevskaya, Contact structures with distinct Heegaard Floer
  invariants, Math. Res. Lett. 11 (2004) (general forward theorem; fixes
  no $W^*/\tau$-pullback pair — background only).
- E. Karakurt, T. Oba, T. Ukida, Planar Lefschetz fibrations and Stein
  structures with distinct Ozsv\'ath–Szab\'o invariants on corks,
  arXiv:1607.07661 (different pair, no $d_3$ gap — contrast case).
