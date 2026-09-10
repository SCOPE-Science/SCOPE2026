# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A parity disproof of the named stem-52 d5 for V(1) at p=3

## Abstract
We disprove the target claim. For $V(1)=S/(3,v_1)$ at prime $3$, the
BP-Adams–Novikov $E_2$ groups $E_2^{3,55}(V(1))$ and $E_2^{8,59}(V(1))$
are both zero, by even-degree concentration of $BP_*$,
$BP_*BP$, $BP_*(V(0))$, $BP_*(V(1))$ and the cobar complex.
Hence there are no nonzero classes $g,h$ in those bidegrees and no
nonzero differential $d_5(g)=h$ up to unit. The $d_5$ degree
$(s,t)\mapsto(s+5,t+4)$ is correct but both endpoint groups vanish.

## 1. Setup and grading

Work $3$-locally, $p=3$. The BP-Adams–Novikov spectral sequence for a
spectrum $X$ has
$$E_2^{s,t}(X)=\mathrm{Ext}^{s,t}_{BP_*BP}(BP_*,BP_*(X))$$
computed by the cobar complex, converging to $\pi_{t-s}(X)_{(3)}$
in good cases. Stem $=t-s$. The named bidegrees are
$$(s,t)=(3,55),\quad t-s=52;\qquad (s,t)=(8,59),\quad t-s=51,$$
and indeed $(3+5,55+4)=(8,59)$, the $d_r$ degree
$d_r:E_r^{s,t}\to E_r^{s+r,t+r-1}$ with $r=5$. This part is not disputed.

Target claim: there exist nonzero $g\in E_2^{3,55}(V(1))$,
$h\in E_2^{8,59}(V(1))$ with $d_5(g)=uh$, $u$ a $3$-adic unit,
witnessed by a Toda shuffle plus motivic comparison.

We show both groups are zero, so the claim is false in the strong sense:
the endpoint $E_2$ terms vanish, not merely the differential.

## 2. Evenness lemmas

**Lemma 1 (coefficients).** $BP_*=\mathbb{Z}_{(3)}[v_1,v_2,\dots]$,
$|v_i|=2(3^i-1)$, is concentrated in even degrees. Likewise
$BP_*BP=BP_*[t_1,t_2,\dots]$, $|t_i|=2(3^i-1)$, is even as a
$BP_*$-algebra: as $BP_*$-module it is free on monomials in the $t_i$,
each of even total degree.

*Proof.* $2(3^i-1)$ is even. Monomial degrees are nonneg integer
combinations of even numbers, hence even. ∎

**Lemma 2 ($V(0)$).** Let $V(0)=\mathrm{cof}(3:S\to S)_{(3)}$.
Then $BP_*(V(0))$ is concentrated in even degrees, with
$BP_{2k}(V(0))\cong BP_{2k}/3$.

*Proof.* LES of the cofiber:
$$\cdots\to BP_k \xrightarrow{\times 3} BP_k \to BP_k(V(0))
\to BP_{k-1}\xrightarrow{\times 3} BP_{k-1}\to\cdots.$$
$BP_{\mathrm{odd}}=0$ by Lemma 1 and $BP_*$ is torsionfree, so
$\times 3$ is injective. If $k$ is odd, $BP_k=0$ and the map
$BP_k(V(0))\to BP_{k-1}$ lands in $\ker(\times 3)=0$ on the torsionfree
$BP_{k-1}$; precisely, exactness gives $BP_k(V(0)}$ injects into
$\ker(BP_{k-1}\xrightarrow{\times3}BP_{k-1})=0$. So $BP_{\rm odd}(V(0))=0$.
If $k$ is even, $BP_{k-1}=0$ so $BP_k(V(0))=\mathrm{coker}(\times3)$.
∎

**Lemma 3 ($V(1)$).** Let $V(1)=\mathrm{cof}(v_1:\Sigma^4V(0)\to V(0))$,
$|v_1|=4$, $f_*=\times v_1$ on $BP_*$. Then $BP_*(V(1))$ is concentrated
in even degrees, $BP_{\rm even}(V(1))\cong BP_{\rm even}/(3,v_1)$.

*Proof.* Write $k$ for total degree. $BP_k(\Sigma^4V(0))=BP_{k-4}(V(0))$.
LES:
$$BP_{k-4}(V(0))\xrightarrow{\times v_1}BP_k(V(0))\to BP_k(V(1))
\to BP_{k-5}(V(0))\xrightarrow{\times v_1}BP_{k-1}(V(0)).$$
Now $BP_*(V(0))=BP_*/3\cong\mathbb{F}_3[v_1,v_2,\dots]$ is a polynomial
ring, hence a domain; $\times v_1$ is injective.
If $k$ is odd: $BP_k(V(0))=0$ by Lemma 2, so
$BP_k(V(1))\cong\ker\big(BP_{k-5}(V(0))\xrightarrow{\times v_1}
BP_{k-1}(V(0))\big)$.
Here $k-5$ and $k-1$ are even, but injectivity forces the kernel to be
$0$. Hence $BP_{\rm odd}(V(1))=0$.
If $k$ is even: $k-5$ is odd so $BP_{k-5}(V(0))=0$ and
$BP_k(V(1))=\mathrm{coker}(\times v_1)$. ∎

Remark: the cells of $V(1)$ in dimensions $0,1,5,6$ do not produce odd
$BP$-classes; $BP_*(V(1))$ is the quotient by the regular sequence
$(3,v_1)$, not a free module on cells.

## 3. Cobar vanishing

**Lemma 4.** For $M=BP_*(V(1))$, $\mathrm{Ext}^{s,t}_{BP_*BP}(BP_*,M)=0$
for all $s$ whenever $t$ is odd.

*Proof.* The (normalized) cobar complex is
$C^s=\bar\Gamma^{\otimes_{BP_*}s}\otimes_{BP_*}M$,
$\Gamma=BP_*BP$, $\bar\Gamma=\ker(\Gamma\to BP_*)$.
By Lemma 1, $\Gamma$ is free over $BP_*$ on even-degree monomials;
$\bar\Gamma$ likewise is spanned in even internal degrees.
By Lemma 3, $M$ is even. An elementary tensor has internal degree equal
to the sum of the degrees of its factors, each even, hence even.
So $C^{s,t}=0$ for $t$ odd. Ext is the cohomology of this complex, so it
vanishes in odd $t$. ∎

## 4. Main theorem (target is false)

**Theorem.** At $p=3$,
$$E_2^{3,55}(V(1))=0,\qquad E_2^{8,59}(V(1))=0.$$
Consequently there are no nonzero classes $g,h$ in those bidegrees and
the claimed identity $d_5(g)=h$ up to $3$-adic unit with $g,h$ nonzero
is impossible. The full Toda-shuffle/motivic-comparison certificate
cannot exist because its endpoints do not exist.

*Proof.* By Lemma 4 with $t=55$ and $t=59$, both odd. ∎

Note this rules out every variant of the witness: any shuffle identity
forcing a nonzero $d_5$ between nonzero classes in these bidegrees, and
any motivic comparison detecting nonzero source/target, must fail at the
$E_2$-existence step. A differential $0\to0$ holds vacuously but does not
satisfy the claim's nonzero requirement.

## 5. Reproducibility

`output/artifacts/verify_parity.py` checks $|v_i|,|t_i|$ evenness,
oddness of $55,59$, the $d_5$ degree $(3,55)\mapsto(8,59)$, monomial
parity, and truncated $v_1$-injectivity; it prints `VERIFY_OK`.
The lemmas above are self-contained and use no external charts.

## 6. Scope

This disproof uses only the standard $BP$ degrees, the two cofiber
sequences defining $V(0),V(1)$, and the cobar description — all textbook
(Ravenel, Adams). It does not decide any other $V(1)$ differential,
does not use $L_2$-localization or motivic comparison, and leaves open
all bidegrees with $t$ even.
