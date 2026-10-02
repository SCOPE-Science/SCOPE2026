# A center-local norm formula for generalized derivations on finite sums of type-I factors

## Result

Let
\[
\mathcal M=\bigoplus_{r=1}^{m} B(H_r),
\]
where each \(H_r\) is a separable infinite-dimensional complex Hilbert space, and equip \(\mathcal M\) with the sum of the standard traces. Let \(E\subset c_0\) be a symmetrically normed sequence space. Write \(C_E(\mathcal M)\) for the corresponding symmetric ideal: if \(x=(x_r)\) has compact coordinates, then
\[
\|x\|_{C_E(\mathcal M)}
 =\left\|\left(\bigoplus_{r=1}^m \mu(x_r)\right)^*\right\|_E,
\]
where \(^*\) denotes decreasing rearrangement of the finite disjoint union of singular-value sequences.

Let \(a=(a_r),b=(b_r)\in C_E(\mathcal M)\) be self-adjoint, and define the generalized derivation
\[
\delta_{a,b}(x)=ax-xb,\qquad x\in\mathcal M.
\]
For each central summand put
\[
g_r=\left[
 \big(\mu((a_r)_+)+\mu((b_r)_-)\big)
 \oplus
 \big(\mu((b_r)_+)+\mu((a_r)_-)\big)
\right]^*,
\]
and let
\[
G=\left(\bigoplus_{r=1}^{m}g_r\right)^*.
\]
Then
\[
\boxed{
\|\delta_{a,b}\|_{\mathcal M\to C_E(\mathcal M)}=\|G\|_E.
}
\]

Thus the exact formula on a finite atomic center is **center-local**: positive singular data from \(a\) can be paired with negative singular data from \(b\), and conversely, only inside the same factor summand. After those local profiles are formed, the profiles are merged and rearranged globally.

This differs from applying the factor formula directly to the global singular-value functions of \(a\) and \(b\), which can pair spectral mass lying in different central summands and can give a strict overestimate.

## Finite-sum uniform-submajorization lemma

We use \(\vartriangleleft\) for uniform submajorization in the sense used by Huang--Pliev--Sukochev--Xu.

If nonnegative measurable functions (or singular-value sequences) \(f_r,h_r\), \(1\le r\le m\), satisfy
\[
f_r\vartriangleleft h_r\qquad(1\le r\le m),
\]
then for every \(\varepsilon>0\),
\[
(1-\varepsilon)
\left(\bigoplus_{r=1}^m f_r\right)^*
\vartriangleleft
\left(\bigoplus_{r=1}^m h_r\right)^*.
\]
More generally, the same conclusion holds if each hypothesis is available with an arbitrarily small multiplicative loss.

Indeed, Proposition 3.1 of Huang--Pliev--Sukochev--Xu states that if \(f_1\vartriangleleft h_1\) and \(f_2\vartriangleleft h_2\), then, for every \(\eta>0\),
\[
(1-\eta)(f_1\oplus f_2)\vartriangleleft h_1\oplus h_2.
\]
Iteration gives the finite-sum statement; the accumulated loss can be made arbitrarily small. This is precisely where finiteness of the center is used.

## Proof of the norm formula

### Upper bound

Let \(u=(u_r)\in\mathcal M\) be unitary. On the \(r\)-th factor,
\[
\delta_{a,b}(u)_r=a_ru_r-u_rb_r.
\]
The proof of Theorem 3.2 in Huang--Pliev--Sukochev--Xu gives, for every \(\eta>0\),
\[
(1-\eta)\mu(a_ru_r-u_rb_r)\vartriangleleft g_r.
\]
Apply the finite-sum lemma to the \(m\) component inequalities. For every \(\varepsilon>0\),
\[
(1-\varepsilon)\mu(au-ub)\vartriangleleft G.
\]
Symmetry of \(E\) and the uniform-submajorization norm principle therefore imply
\[
(1-\varepsilon)\|au-ub\|_{C_E(\mathcal M)}\le \|G\|_E.
\]
Letting \(\varepsilon\downarrow0\) gives
\[
\|au-ub\|_{C_E(\mathcal M)}\le \|G\|_E.
\]
The Russo--Dye theorem then yields
\[
\|\delta_{a,b}\|_{\mathcal M\to C_E(\mathcal M)}\le \|G\|_E.
\]

### Lower bound

The type-\(I_\infty\) case of the lower-estimate construction underlying Lemma 4.2 of Huang--Pliev--Sukochev--Xu is explicitly stated there to follow by the same argument as the displayed infinite-factor case. Applied to the compact self-adjoint pair \((a_r,b_r)\), it gives the following atomic counterpart. For every integer \(N\ge2\), there is a partial isometry \(v_{r,N}\in B(H_r)\) such that, with
\[
c_N=\frac{N-1}{N},\qquad \alpha_N=\frac{N}{N+1},
\]
we have
\[
c_N\,\sigma_{\alpha_N}g_r
\le
\mu(a_rv_{r,N}-v_{r,N}b_r).
\]
Here \(\sigma_\alpha f(s)=f(s/\alpha)\) is the dilation convention of that paper, with sequences represented by their unit-step functions.

Set
\[
v_N=(v_{1,N},\ldots,v_{m,N})\in\mathcal M.
\]
Then \(\|v_N\|\le1\). Distribution functions add under finite disjoint unions, and therefore dilation commutes with finite disjoint union after rearrangement:
\[
\left(\bigoplus_{r=1}^m \sigma_{\alpha_N}g_r\right)^*
=
\sigma_{\alpha_N}G.
\]
Consequently,
\[
c_N\sigma_{\alpha_N}G
\le
\mu(av_N-v_Nb).
\]

For \(0<\alpha\le1\), equation (4) of Huang--Pliev--Sukochev--Xu states
\[
\alpha G\vartriangleleft \sigma_\alpha G.
\]
Multiplying by \(c_N\) and using \(c_N\alpha_N=(N-1)/(N+1)\), we obtain
\[
\frac{N-1}{N+1}G
\vartriangleleft
c_N\sigma_{\alpha_N}G
\le
\mu(av_N-v_Nb).
\]
Hence
\[
\frac{N-1}{N+1}\|G\|_E
\le
\|av_N-v_Nb\|_{C_E(\mathcal M)}
\le
\|\delta_{a,b}\|_{\mathcal M\to C_E(\mathcal M)}.
\]
Letting \(N\to\infty\) proves the reverse inequality and hence the theorem. \(\square\)

## A strict obstruction to global cross-center pairing

The center-locality is necessary even for two summands.

Let
\[
\mathcal M=B(H)\oplus B(H),
\]
where \(H\) is infinite-dimensional, let \(p\) be a rank-one projection, and for \(1<q<\infty\) take \(E=\ell_q\), so the target is the corresponding Schatten ideal over the two summands. Put
\[
a=(p,0),\qquad b=(0,-p).
\]
For \(x=(x_1,x_2)\) with \(\|x\|=\max(\|x_1\|,\|x_2\|)\le1\),
\[
\delta_{a,b}(x)=(px_1,x_2p).
\]
Both coordinates have rank at most one and singular value at most one, so
\[
\|\delta_{a,b}(x)\|_q\le 2^{1/q}.
\]
Taking \(x=(1,1)\) gives equality. Thus
\[
\boxed{\|\delta_{a,b}\|=2^{1/q}.}
\]
The center-local profile \(G\) consists of two unit singular values and gives exactly \(2^{1/q}\).

By contrast, the global singular-value functions of \(a_+\) and \(b_-\) are both the one-point sequence \((1,0,\ldots)\). Substituting them into the factor-style expression before respecting the center gives \((2,0,\ldots)\), whose \(\ell_q\)-norm is \(2\). Hence the general upper estimate from Theorem 3.2 can be strict on a non-factor:
\[
2^{1/q}<2\qquad(1<q<\infty).
\]
The discrepancy is exactly the forbidden cross-center pairing of the two rank-one pieces.

## Relation to the positive non-factor theorem

When \(a,b\ge0\), each local profile is simply
\[
g_r=\mu(a_r)\oplus\mu(b_r).
\]
Their finite disjoint union rearranges to the singular-value function of \(a\oplus b\). The center-local formula therefore reduces to
\[
\|\delta_{a,b}\|=\|a\oplus b\|,
\]
in agreement with Theorem 1.3 of Huang--Pliev--Sukochev--Xu for positive implementers on properly infinite semifinite von Neumann algebras.

The new point is the self-adjoint sign-changing case: the factor theorem remains exact on each central component, but its positive/negative matching must not be performed across different central components.

## Scope and limitations

- The theorem is stated for a **finite** direct sum of infinite type-I factors. The proof uses finite stability of uniform submajorization. Huang--Pliev--Sukochev--Xu explicitly note that an analogous direct-sum statement used later in their paper fails for infinite direct sums. This does not prove that the norm formula above fails for an infinite atomic center; no such claim is made here.
- The implementers are self-adjoint members of the symmetric compact ideal. The result does not address general non-self-adjoint implementers.
- The lower-bound proof uses the atomic type-\(I_\infty\) counterpart of the construction behind Lemma 4.2 in the cited paper; the authors explicitly state that the atomic case follows by the same argument.
- Originality is claimed only to the best of our knowledge. The 2026 primary source was inspected in full in the sections containing Theorems 1.1--1.3, Theorem 3.2, Proposition 3.1, Lemma 4.2, Remark 4.3 and Proposition 5.2. The older Fialkow (1979) and Fialkow--Loebl (1984) papers were identified and their role was checked through the 2026 source and accessible bibliographic material, but their complete texts were not inspected here. Those papers are therefore the main residual literature risk.

## Literature context

Huang, Pliev, Sukochev and Xu give the exact self-adjoint formula on an infinite semifinite **factor** and a positive-operator formula on general properly infinite semifinite von Neumann algebras. Their Remark 4.3 observes that the factor hypothesis cannot simply be removed in the self-adjoint setting, using an abelian obstruction. The finite atomic-center formula above identifies an intermediate non-factor class where an exact self-adjoint formula survives after replacing global sign matching by center-local matching.

Targeted searches for finite-center, finite-direct-sum, central-summand and equivalent formulations of generalized-derivation norm formulas did not locate this statement or the two-summand cross-center obstruction above.

## References

1. J. Huang, M. Pliev, F. Sukochev, R. Xu, *Norms of generalized derivations with values in symmetric spaces*, Advances in Mathematics **495** (2026), 110964; arXiv:2609.15233.
2. L. A. Fialkow, *A note on norm ideals and the operator \(X\mapsto AX-XB\)*, Israel J. Math. **32** (1979), 331--348.
3. L. A. Fialkow, R. Loebl, *Elementary mappings into ideals of operators*, Illinois J. Math. **28** (1984), 555--578.
4. A. Ber, J. Huang, F. Sukochev, *Norms of skew-adjoint derivations with values in the predual of a semifinite von Neumann algebra*, J. Funct. Anal. **285** (2023), 110072.
