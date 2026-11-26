# A sharp central-to-distributed fuel-break budget transition on a four-site forest corridor

## Finding

For a four-site forest corridor with three independently permeable fire-spread links, uniform single-site ignition, baseline link permeability \(p\in(0,1]\), and a fixed nonnegative treatment budget \(B\), suppose effort \(x_i\geq0\) on link \(i\) changes its permeability to \(q_i=p e^{-x_i}\), subject to \(x_1+x_2+x_3=B\). Define risk as the expected final number of burned sites under a single ignition. The risk-minimizing allocation exists and is unique, and has the following complete phase diagram:

- For \(0\leq B\leq \log(1+p)\), the unique optimum is \((x_1,x_2,x_3)=(0,B,0)\): spend everything on the center link.
- For \(B>\log(1+p)\), write \(z>1\) for the unique solution of \(z^3+p z^2=e^B\). The unique optimum is

\[
(x_1,x_2,x_3)=\bigl(\log z,\log(z+p),\log z\bigr).
\]

All three links then receive positive treatment; the middle link always receives strictly more than either outer link. Moreover \(x_2-x_1=\log(1+p/z)\) decreases strictly with \(B\) and tends to zero; every allocation fraction tends to \(1/3\). Among paths with two, three or four sites, four sites are the first to admit this budget-induced onset of positive treatment on previously unprotected outer links: in the three-site path the two links always receive equal effort \(B/2\) for \(B>0\).

## Assumptions and scope

The sites are \(1,2,3,4\), joined only by links \(12,23,34\). Exactly one site is ignited, uniformly at random and independently of link status. For given effort allocations, each link independently transmits fire with probability \(q_i=p e^{-x_i}\); the final fire consists precisely of sites connected to the ignition in the resulting open-link graph (no time limits, re-ignition, wind, spotting, or firefighting). The objective is expected *site count*, not monetary damages, tail risk or actual burned acreage. Effort is divisible and has an assumed exponential effect on transmission, with normalized aggregate budget \(B\). No environmental calibration is asserted.

## Proof

1. For any two distinct sites on a tree, both belong to the same open cluster precisely when all edges on their unique connecting path are open. If \(U\) is the uniform ignition and \(S\) is its open-cluster size, linearity of expectation gives \(\mathbb E S=1+(2/4)\sum_{i<j}\Pr(i\leftrightarrow j)\), since each unordered connected pair contributes twice when summing over the possible ignitions. Independence therefore gives the *exact* formula

\[
R=1+\frac12\bigl(q_1+q_2+q_3+q_1q_2+q_2q_3+q_1q_2q_3\bigr).
\]

2. Fix central effort \(y=x_2\) and hence the outer sum \(x_1+x_3=B-y\). Substitution into \(R\) shows that all terms dependent on how the outer sum is split equal the positive factor \((p/2)(1+p e^{-y})\) times \(e^{-x_1}+e^{-x_3}\); the three-link product is constant for fixed \(B\). Strict convexity of the exponential or strict AM–GM shows this sum is uniquely minimized by \(x_1=x_3=(B-y)/2\). Thus every global minimizer is reflection symmetric.

3. Write \(x_1=x_3=x\), \(x_2=B-2x\), \(0\leq x\leq B/2\). Apart from the positive constant term \(1+(p^3/2)e^{-B}\), the objective is

\[
F(x)=\frac12\bigl(2p e^{-x}+p e^{-B+2x}+2p^2 e^{-B+x}\bigr).
\]

Its first and second derivatives are

\[
F'(x)=p\bigl(-e^{-x}+e^{-B+2x}+p e^{-B+x}\bigr),
\quad
F''(x)=p\bigl(e^{-x}+2e^{-B+2x}+p e^{-B+x}\bigr)>0.
\]

The left-boundary sign is \(F'(0)=p\{(1+p)e^{-B}-1\}\). For all \(B>0\), the right-boundary derivative \(F'(B/2)=p\{1+(p-1)e^{-B/2}\}>0\). Strict convexity now establishes the unique center-only optimum when \(B\leq\log(1+p)\), and a unique strictly interior \(x\) otherwise. When \(B=0\), the sole feasible allocation is zero and agrees with the result.

4. At an interior optimum \(F'(x)=0\). Multiplying this equality by \(e^{B+x}\) yields \(e^B=e^{3x}+p e^{2x}\). Setting \(z=e^x\) gives the claimed cubic. Since \(z\mapsto z^3+pz^2\) is strictly increasing on \([1,\infty)\), \(z>1\) exists uniquely exactly when \(e^B>1+p\). The budget equation then yields \(B=2\log z+\log(z+p)\) and central effort \(B-2x=\log(z+p)>\log z\). Differentiating the increasing cubic implicitly shows that \(z\) strictly increases with \(B\), so the positive gap \(\log(1+p/z)\) strictly decreases. The cubic gives \(z\sim e^{B/3}\) and therefore the stated large-budget limit.

5. A two-site path has just one link. For a three-site path with two links, the exact uniform-ignition risk is \(1+(2/3)(q_1+q_2+q_1q_2)\). Under fixed \(B=x_1+x_2\), the product is constant and the sum \(e^{-x_1}+e^{-x_2}\) has a unique minimum at \(x_1=x_2=B/2\). Hence the four-site path is minimal *among paths of two to four sites* for the central-only to all-positive budget transition.

## Verification

The accompanying `check.py` enumerates all eight independent edge states and four ignition sites, confirming the pair-connectivity risk formula on a grid of rational probabilities; it also checks the allocation equations over a deterministic parameter grid. For an exact rational comparison, choose \(p=1/2\), \(B=\log2>\log(3/2)\). Center-only treatment produces open-link probabilities \((1/2,1/4,1/2)\) and risk \(57/32\). The feasible split \((\log(9/8),\log(128/81),\log(9/8))\) produces open-link probabilities \((4/9,81/256,4/9)\) and risk \(8177/4608<57/32\), verifying a strictly beneficial onset of outer treatment. The analytic derivative and convexity arguments, not these finite checks, prove the theorem for all allowed \(p,B\).

## Relationship to prior work

Ager et al. (2023) motivate the operational choice between concentrating firebreak treatments and distributing treatments across networks, using large-scale spatial planning and simulated fires; their complete open-access article does not derive the four-site Bernoulli-link phase boundary. Yemshanov et al. (2021) optimize which forest-network nodes to protect using estimated spread probabilities and discrete network treatments, a different objective and action. Somers and Manchester (2020) provide broad exponential-cost resource allocation under linearized continuous-time spreading dynamics and convex programming; their paper does not state this exact independent-bond, uniform-ignition four-site susceptibility identity or its cubic phase diagram. Existing general convexity and pair-connectivity principles are not claimed new. Related network interdiction and percolation work may contain equivalent results under different terminology, so historical priority is provisional.

## Limitations

The theorem is exact only for a four-site path with uniform one-site ignition, independent undirected link statuses, homogeneous baseline probability, exponential treatment response and divisible budget. It does not model fire arrival timing, wind, ember spotting, heterogeneous site values, fire suppression, spatially correlated failures or real-world treatment costs. The three-site comparison is restricted to paths. The model does not imply a field management prescription without calibration and uncertainty analysis. No independent validation is asserted.

## References

- Ager, A. A., Day, M. A., Aparício, B. A., Houtman, R. & Stinchfield, A. (2023). *Optimizing the implementation of a forest fuel break network*. PLOS ONE 18(12), e0295392. First publicly published 2023-12-13. https://doi.org/10.1371/journal.pone.0295392
- Yemshanov, D. et al. (2021). *Detecting critical nodes in forest landscape networks to reduce wildfire spread*. PLOS ONE 16(10), e0258060. https://doi.org/10.1371/journal.pone.0258060
- Somers, V. L. J. & Manchester, I. R. (2020). *Sparse Resource Allocation for Control of Spreading Processes via Convex Optimization*. arXiv:2003.07555. https://arxiv.org/abs/2003.07555
