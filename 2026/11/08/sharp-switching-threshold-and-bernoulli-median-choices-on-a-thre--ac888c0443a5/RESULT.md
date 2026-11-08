# Sharp switching threshold and Bernoulli median choices on a three-agent path

## Finding

For the original **discrete-neighbor weighted-median** synchronous update of Mohr, Hjorth, and Porter, a connected three-vertex path has a sharp transition at self-appraisal \(s=2/3\). Every initial configuration reaches opinion consensus for all \(0<s<1\), but the identity of the central agent's selected median neighbor eventually becomes constant for every initial configuration when \(s\leq 2/3\). For \(s>2/3\), it switches infinitely many times for all initial central opinions except a countable exceptional set, provided the two initial leaf opinions are distinct.

At \(s=3/4\), with the initial center opinion uniform on a suitable interval between or around the two fixed initial leaf opinions, the successive selected-neighbor symbols form *independent fair binary choices*, even though the three real-valued opinions converge to a common deterministic limit for each realization of the initial condition. The randomness is only in the sampled initial center opinion; subsequent updating is deterministic.

## Assumptions and scope

Take the three-vertex path with center \(C\) and leaves \(A,B\). Initially \(0\le a_0<b_0\le1\) and \(0\le c_0\le1\). The center places weight \(1/2\) on each leaf and each leaf places weight \(1\) on the center, with no self-loop weights. All agents synchronously update by
\[
 a_{t+1}=(1-s)a_t+s c_t,\qquad
 b_{t+1}=(1-s)b_t+s c_t,\qquad
 c_{t+1}=(1-s)c_t+s\,M_t,
\]
where \(0<s<1\) and \(M_t\in\{a_t,b_t\}\) is whichever leaf opinion is nearer to \(c_t\), breaking a distance tie in favor of the smaller leaf opinion \(a_t\). This is the discrete-neighbor selection used by the **original 2024 version** of arXiv:2406.17552. It must not be replaced by the continuum of real weighted-median minimizers used in its revised 2025 version.

Set \(q=1-s\), \(m_t=(a_t+b_t)/2\), \(d_t=(b_t-a_t)/2>0\), \(z_t=c_t-m_t\), \(h_t=(c_t+m_t)/2\), and \(w_t=z_t/d_t\). Define \(\sigma(w)=1\) for \(w>0\) and \(\sigma(w)=-1\) for \(w\le0\), respecting the lower-leaf tie convention.

The qualitative threshold is a statement about eventual **median-neighbor selection**, not the convergence rate of the opinions. When \(a_0=b_0\), neighbor selection has no distinct alternatives and all opinions still converge; the switching classification is therefore asserted only for \(a_0<b_0\).

## Proof

**Exact reduction.** Directly from the three synchronous updates, the leaf separation is \(d_{t+1}=q d_t\), the normalized central displacement obeys
\[
 w_{t+1}=T_s(w_t):=
 \frac{1-2s}{1-s}w_t+\frac{s}{1-s}\sigma(w_t),
\]
and \(h_{t+1}=h_t+(s/2)\sigma(w_t)d_t\). In particular \(d_t=q^t d_0\) and the exact limiting consensus, once convergence is justified, is
\[
 L=h_0+\frac{s d_0}{2}\sum_{t=0}^{\infty}q^t\sigma(w_t).
\]
All states remain in \([0,1]\) because each update is a convex combination of existing opinions.

**Universal opinion consensus.** The unnormalized difference satisfies
\[
 z_{t+1}=(1-2s)z_t+s\sigma(w_t)d_t.
\]
Because \(0<s<1\), both \(q<1\) and \(|1-2s|<1\). Iterating \(|z_{t+1}|\le |1-2s||z_t|+s q^t d_0\) shows \(z_t\to0\) (including the coincident-rate case, where the bound is polynomial times a decaying exponential). Also \(\sum_t|h_{t+1}-h_t|\le d_0/2\), so \(h_t\to L\). Since \(a_t=h_t-z_t/2-d_t\), \(b_t=h_t-z_t/2+d_t\), and \(c_t=h_t+z_t/2\), all three opinions converge to \(L\).

**Finite switching for \(s\le2/3\).** For \(s\le1/2\), the two coefficients in \(T_s\) are nonnegative, so no nonzero sign can change; the tie at zero immediately selects the negative branch. Suppose \(1/2<s\le2/3\). Put \(\alpha=(2s-1)/(1-s)\in(0,1]\) and \(B=\alpha+1=s/(1-s)\). Then \(T_s(w)=-\alpha w+B\sigma(w)\). If \(0<|w|\le B/\alpha\), its next value has the same sign or is exactly zero; after a nonzero step, its magnitude is at most \(B\le B/\alpha\), so it cannot later switch sign. An exact zero selects the negative branch and maps to \(-B\), after which the sign is negative indefinitely. If \(|w|>B/\alpha\), the next nonzero value has opposite sign and magnitude \(\alpha|w|-B\), which is **strictly less** than \(|w|\) by at least \(B\) for \(\alpha\le1\). Hence after finitely many changes the orbit enters the non-switching region. The borderline \(s=2/3\) is included.

**Infinite switching for \(s>2/3\) outside countably many starts.** Here \(\alpha>1\). If the sign were eventually constant, equal to \(\varepsilon\in\{-1,1\}\), then thereafter the recurrence would be \(w_{t+1}=-\alpha w_t+(\alpha+1)\varepsilon\), with repelling fixed point \(\varepsilon\). Its explicit solution \(w_{N+k}=\varepsilon+(-\alpha)^k(w_N-\varepsilon)\) can remain on the same signed half-line for all \(k\) only if \(w_N=\varepsilon\). Consequently the exceptional set of eventually constant-sign orbits is contained in
\[
 E_s=\bigcup_{N\ge0}T_s^{-N}(\{-1,1\}),
\]
which is countable because \(T_s\) has two affine injective branches. Conversely an orbit that lands at \(1\) or \(-1\) remains fixed. Thus the exceptional set is exactly \(E_s\) and every other initial normalized displacement switches its sign infinitely often. With fixed distinct leaves, the affine map \(c_0\mapsto w_0\) preserves countability; almost every admissible initial center opinion therefore switches infinitely often.

**Fair Bernoulli itinerary at \(s=3/4\).** Now \(T_s(w)=3\sigma(w)-2w\). Up to the measure-zero endpoints, each of the two intervals \((-3,0)\) and \((0,3)\) maps bijectively onto \((-3,3)\) with slope \(-2\). Their union is forward-invariant modulo endpoints. Every prescribed length-\(k\) sign word determines, up to endpoints, one interval of initial normalized displacements of length \(6/2^k\). Therefore, if \(w_0\) is uniform on \([-3,3]\), the probability of each specified length-\(k\) word is exactly \(2^{-k}\), proving that \(\sigma(w_0),\sigma(w_1),\ldots\) is an independent fair-sign process. This is realized entirely within \([0,1]\): choose \((a_0,b_0)=(2/5,3/5)\) and let \(c_0\) be uniform on \([1/5,4/5]\), so \(w_0\) is uniform on \([-3,3]\). Consensus still follows from the previous contraction argument for each starting point.

**Explicit infinite-switching witness.** At \(s=3/4\), start from \((a_0,c_0,b_0)=(2/5,9/10,3/5)\). Then \(w_0=4\) and induction gives \(w_t=(-1)^t(3+2^t)\). The selected neighbor alternates at **every step**, while the consensus formula gives \(L=73/100\). Two agents cannot exhibit this phenomenon because each has only one possible neighbor, making three agents minimal in connected simple graphs.

## Verification

`verify.py` uses exact rational arithmetic. It checks 7,776 identities between direct opinion updates and the reduced map, including ties and both sides of the parameter threshold; 1,022 finite-word preimage intervals up to word length nine for the Bernoulli coding; 372 initial configurations with subcritical or critical self-appraisal for finite eventual switching; and twenty steps of the explicit alternating witness. Execute `python verify.py`. The infinite-time claims follow from the proofs above, not from finite tests.

## Relationship to prior work

Mohr, Hjorth, and Porter's first public arXiv version (2024) introduced the synchronous, self-appraised *neighbor-valued* weighted median and investigated numerical final distributions and a mean-field approximation. The present theorem resolves a distinct exact small-network question: when the selected median neighbor stabilizes, and how a full Bernoulli switching itinerary can coexist with consensus. The 2025 revised arXiv version (and later journal presentation) broadens the allowable weighted median from neighbor values to **arbitrary real minimizers**, closest to the current opinion. On two equal-weight neighbors that revised choice is projection onto their interval, whereas the original 2024 choice is the nearest endpoint. The theorem deliberately applies **only to the original 2024 rule** and makes no claim for that revised rule.

Mei and collaborators' earlier median-based opinion dynamics use different asynchronous updates and focus on convergence, consensus and dissensus of the real-valued states. Those results neither assert nor imply the specific path's switching threshold or its Bernoulli symbolic law. The full-shift coding itself is a standard fact of piecewise expanding maps; the application and the precise reduction in this opinion model are the claimed contributions.

## Limitations

The graph is the three-node path with equal center influence weights and positive common self-appraisal. The Bernoulli conclusion applies to the specified uniform distribution of *initial* center opinions, not to repeated random updates. It does not assert infinite opinion oscillation, instability of consensus, or a result for the revised real-minimizer median. The originality comparison is a best-knowledge literature check and not an independent priority certificate; an unindexed equivalent may exist.

## References

1. L. Mohr, P. G. Hjorth, and M. A. Porter, *A Weighted-Median Model of Opinion Dynamics on Networks*, arXiv:2406.17552v1, first submitted 2024-06-25, especially Section 2.2 (original neighbor-valued weighted median), https://arxiv.org/abs/2406.17552.
2. L. Mohr, P. G. Hjorth, and M. A. Porter, *Long-Time and Short-Time Dynamics in a Weighted-Median Opinion Model on Networks*, arXiv:2406.17552v3, posted 2025-07-31, especially Section 2.2 (different real-minimizer rule), https://arxiv.org/html/2406.17552v3.
3. W. Mei, J. M. Hendrickx, G. Chen, F. Bullo, and F. Dörfler, *Convergence, Consensus, and Dissensus in the Weighted-Median Opinion Dynamics*, IEEE Transactions on Automatic Control 69 (2024), 6700–6714, https://doi.org/10.1109/TAC.2024.3376752.
