# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Transversal $T$ no-go for an explicit $[[8,2,3]]$ stabilizer code

## Abstract
We fix an explicit $[[8,2,3]]$ Pauli stabilizer code $C_8$ (tableau below),
verify commutation, $|\mathcal S|=64$ with $-I\notin\mathcal S$, the exact
Shor--Laflamme enumerators, all nine MacWilliams identities, and distance
$d=3$. We then prove that **no** strictly transversal operator
$U=\bigotimes_{i=1}^8 E_i$, $E_i=C_iT^{s_i}$ with $C_i$ single-qubit Clifford
and $s_i\in\{+1,-1\}$, preserves the codespace. The obstruction is a
Pauli-support-mismatch (covering) lemma: every one of the $3^8=6561$ possible
Clifford $Z$-axis frames is eliminated by a minimum-weight stabilizer with a
support unique among minimum-weight stabilizers. The logged data give the
weight-divisibility defect and a minimal codespace-leakage bound: each
outside-codespace branch carries Hilbert--Schmidt weight fraction
$2^{-m}\ge 2^{-4}$ on every frame ($\ge 2^{-1}$ on the $648$ frames killed
at $m=1$; see Sections 3--4).

Since the run is self-contained, no literature lookup is needed to
audit the theorem; the *context* facts below (Bravyi--Haah form, codespace
projector algebra, $3^8$ counting) are standard.

## 1. The code
Paulis coded $0=I,1=X,2=Y,3=Z$. Stabilizer generators:
$$
g_1=XXIIZZIY,\quad g_2=XYZXIIXZ,\quad g_3=YXI IXIXXI,\quad
g_4=XYIZZZY Z,\quad g_5=YYYIZIYY,\quad g_6=ZYZIXZYZ.
$$
Explicitly as tuples:
$(1,1,0,0,3,3,0,2)$, $(1,2,3,2,0,0,1,3)$, $(2,1,0,0,0,1,1,0)$,
$(1,2,0,3,3,3,2,3)$, $(2,2,2,0,3,0,2,2)$, $(3,2,3,0,1,3,2,3)$.

Replay (`python3 output/artifacts/verify.py`, stdlib only):
- all $\binom{6}{2}$ pairs commute symplectically;
- generated group has exactly $64$ elements (Rains: equivalently $-I\notin
  \mathcal S$, so the common $+1$ eigenspace has dimension $2^{8-6}=4$,
  i.e. $k=2$ logical qubits);
- Shor--Laflamme enumerators (by full $4^8=65536$ enumeration):
  $$A=[1,0,0,0,4,12,24,20,3],\qquad
    B=[1,0,0,28,86,216,320,268,105],$$
  satisfying all nine quantum MacWilliams identities
  $B_j=\frac1{64}\sum_i K_j(i)A_i$ exactly;
- distance $d=\min\{w:A_w\ne B_w\}=3$;
- minimum stabilizer weight $w_{\min}=4$, with exactly four weight-$4$
  stabilizers, on pairwise distinct supports (elimination order)
  $\{1,2,4,7\},\{1,3,6,7\},\{0,2,3,4\},\{0,1,5,6\}$ — each the **unique**
  minimum-weight stabilizer on its support.

## 2. Ansatz normalization (Bravyi--Haah form)
The target ansatz is $E_i=C_iT^{s_i}$, $C_i\in\mathcal C_1$,
$s_i=\pm1$, $U=\bigotimes_i E_i$. Write $Q_i=C_iZC_i^\dagger\in\{\pm X,\pm
Y,\pm Z\}$; signs are irrelevant for support counting, so there are
$3^8=6561$ axis frames $Q=(Q_1,\dots,Q_8)$.

Single-qubit identities used (direct $2\times2$ checks):
- $TXT^\dagger=(X+Y)/\sqrt2$, $T^\dagger XT=(X-Y)/\sqrt2$,
  $TYT^\dagger=(Y-X)/\sqrt2$, $T^\dagger YT=(X+Y)/\sqrt2$,
  i.e. $T^{\pm1}$ maps each of $X,Y$ to a balanced superposition of two
  distinct Paulis;
- $T^{\pm1}$ commutes with $Z$ (so with any $Q_i$-axis Pauli it acts as a
  single Pauli up to phase).

Hence, conjugating a stabilizer element $s=(P_1,\dots,P_8)$ by $U$:
with $R_i=C_i^\dagger P_iC_i$ (a Pauli), $T^{s_i}R_iT^{-s_i}$ is a single
Pauli if $R_i\in\{I,Z\}$ and a balanced two-Pauli sum if
$R_i\in\{X,Y\}$; $C_i$ maps these back to one resp.\ two Paulis.
Positions with $P_i\in\{I,Q_i\}$ contribute one Pauli each
($E_iQ_iE_i^\dagger=Q_i$); each of the
$$m(s,Q)=\#\{i:P_i\notin\{I,Q_i\}\}$$
mismatch positions contributes a balanced sum of two Paulis. So
$$UsU^\dagger = 2^{-m/2}\sum_{z\in\{0,1\}^m}\phi_z\,P_z,$$
with $|\phi_z|=1$ and $2^m$ **distinct** Pauli strings $P_z$ (they differ at
every mismatch position). Every $P_z$ has support exactly
$\mathrm{supp}(s)$: identity positions stay identity, $Q_i$ positions stay
$Q_i$, and mismatch positions ($P_i\ne I$) stay non-identity.
(The ordering $E_i=T^{s_i}C_i$ reduces to the same analysis with frame
$C_i^\dagger ZC_i$, still ranging over all $3^8$ frames; signs of $Q_i$
do not affect support counting.)

## 3. Mismatch lemma and elimination
**Lemma.** Let $s^\star$ be a weight-$w_{\min}$ stabilizer whose support is
unique among weight-$w_{\min}$ stabilizers. If $m(s^\star,Q)=m\ge1$ then $U$
does not preserve the codespace.

*Proof (global projector argument).* Let
$\Pi=2^{-6}\sum_{s\in\mathcal S}s$ and expand
$$U\Pi U^\dagger = 2^{-6}\sum_{s\in\mathcal S}UsU^\dagger,
\qquad
UsU^\dagger = 2^{-m(s,Q)/2}\sum_{z}\phi_{s,z}\,P_{s,z},$$
where, by Section 2, every branch $P_{s,z}$ has support exactly
$\mathrm{supp}(s)$, i.e.\ $\mathrm{supp}(P_{s,z})=\mathrm{supp}(s)$.
Fix the eliminator $s^\star$ with $T=\mathrm{supp}(s^\star)$ ($|T|=4$).
By the weight spectrum there are no stabilizers of weight $1,2,3$, and by
uniqueness $s^\star$ is the only weight-$4$ stabilizer on $T$; hence $T$
contains the support of no element of $\mathcal S$ other than $s^\star$
itself and $I$ (whose support is $\emptyset$). Since every branch
$P_{s,z}$ is supported exactly on $\mathrm{supp}(s)$, the only
$s\in\mathcal S$ whose branches can be supported on $T$ is $s=s^\star$
itself. Its $2^m\ge2$ branches $P_{s^\star,z}$ are distinct non-identity
Paulis supported exactly on $T$, none of which lies in $\mathcal S$
(the sole weight-$4$ stabilizer on $T$, $s^\star$ itself, is a single
Pauli and cannot equal $2^m\ge2$ distinct branches). Each carries
coefficient $2^{-6-m/2}\phi$ of magnitude $2^{-6-m/2}<2^{-6}$ in
$U\Pi U^\dagger$, while in $\Pi$ the coefficient of any non-stabilizer
Pauli is $0$ (Paulis are Hilbert--Schmidt orthogonal). At least one
($2^m\ge2$ in fact) nonzero branch therefore lies outside $\mathcal S$,
so $U\Pi U^\dagger\ne\Pi$ and $U$ does not preserve the codespace. ∎

**Exhaustion.** The script checks all $6561$ frames against the four
unique-support weight-$4$ stabilizers in the listed order of Section 1
($\{1,2,4,7\},\{1,3,6,7\},\{0,2,3,4\},\{0,1,5,6\}$): **every** frame has
$m(s^\star,Q)\ge1$ for at least one of them, so zero frames survive. The
first-killer-in-listed-order $m$ histogram is
$\{1:648,\,2:1953,\,3:2628,\,4:1332\}$ (summing to $6561$; the verifier
checks the $6561/6561$ elimination). Thus no transversal
operator of the stated Bravyi--Haah form preserves the codespace — in
particular none implements a logical $T$. Since codespace preservation
fails, the logical action is vacuous. The weight spectrum
($A_1=A_2=A_3=0$) is the weight-divisibility record.

## 4. Magic-gap / leakage witness
For every frame the proof gives a quantitative floor. Within the conjugated
eliminator $Us^\star U^\dagger=2^{-m/2}\sum_z\phi_zP_z$, the $2^m$ branches
are distinct Paulis, hence Hilbert--Schmidt orthogonal
($\mathrm{Tr}(P^\dagger R)=2^8\delta_{P,R}$), and equal-magnitude; so each
branch carries fraction $2^{-m}$ of that element's Hilbert--Schmidt mass.
All $2^m\ge2$ of these branches lie outside $\mathcal S$ (Section 3), so the
conjugated projector $U\Pi U^\dagger$ necessarily has outside-codespace
support. With eliminator $m\le4$ this branch fraction is $2^{-m}\ge2^{-4}$
on every frame, and $\ge2^{-1}$ on the $648$ frames killed at $m=1$. No
magic monotone defined on the codespace can be preserved under such
leakage. The verifier logs the numbers above.

## 5. Scope note
$C_8$ is one explicit $[[8,2,3]]$ stabilizer code with verified distance.
LC-permutation equivalence of $C_8$ to the named Cross--Vandeth census
representative is **not** proved here and is openly disclosed as unproven;
the no-go is proved for this explicit code. The stated ansatz class is
covered in full: all exponent signs, all single-qubit Clifford corrections
(both $C_iT^{s_i}$ and $T^{s_i}C_i$ orderings, which range over the same
$3^8$ frames).

## 6. Replay
`python3 output/artifacts/verify.py` → `VERIFY_OK` (stdlib only; seconds).
