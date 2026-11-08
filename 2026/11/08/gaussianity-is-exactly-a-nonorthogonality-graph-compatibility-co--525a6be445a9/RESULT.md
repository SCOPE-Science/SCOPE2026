# Gaussianity is exactly a nonorthogonality-graph compatibility condition for noisy randomized Kaczmarz

## Finding

Let \(d\ge1\) and \(m\ge d\). Fix unit vectors \(u_1,\ldots,u_m\in\mathbb R^d\) spanning \(\mathbb R^d\), probabilities \(p_i>0\) with \(\sum_i p_i=1\), and positive measurement-noise variances \(s_i>0\). Independently at every iteration choose \(I_k\) with probabilities \(p_i\), draw \(\varepsilon_k\mid I_k=i\sim N(0,s_i)\) independently of all preceding choices, and update the error relative to a consistent noiseless solution by

\[
X_{k+1}=(I-u_{I_k}u_{I_k}^{\mathsf T})X_k+u_{I_k}\varepsilon_k.
\]

The chain has exactly one stationary law \(\pi\), with finite moments of every fixed order. Define the *nonorthogonality graph* on \(\{1,\ldots,m\}\), with an edge \(i\sim j\) exactly when \(u_i^{\mathsf T}u_j\ne0\). Then the following are equivalent:

1. \(\pi\) is a (possibly degenerate) multivariate Gaussian distribution.
2. \(s_i=s_j\) on every edge of this graph.
3. The variances \(s_i\) are constant on each connected component of the graph.

When they hold, if \(V_C=\operatorname{span}\{u_i:i\in C\}\) and \(\Pi_C\) projects orthogonally onto \(V_C\), then the graph components are mutually orthogonal and

\[
\pi=N\left(0,\sum_C s_C\Pi_C\right).
\]

In particular, on a connected graph Gaussian stationary error occurs **if and only if all the fresh row-noise variances coincide**, independently of every positive row-selection probability. If this condition fails, the stationary law is non-Gaussian and some real unit direction \(v\) has strictly positive fourth cumulant,

\[
\operatorname{cum}_4(v^{\mathsf T}X)
=\mathbb E[(v^{\mathsf T}X)^4]-3\mathbb E[(v^{\mathsf T}X)^2]^2>0,
\qquad X\sim\pi.
\]

Moreover, let \(S=\mathbb E_\pi[XX^{\mathsf T}]\), \(P_i=I-u_i u_i^{\mathsf T}\), and \(S_i=P_iSP_i+s_i u_i u_i^{\mathsf T}\). Each unit direction obeys the computable lower bound

\[
\operatorname{cum}_4(v^{\mathsf T}X)
\ge 3\sum_{i=1}^m p_i\bigl(v^{\mathsf T}(S_i-S)v\bigr)^2\ge0.
\]

The classification and the strict non-Gaussianity claim hold for any number of rows, including overdetermined systems.

## Assumptions and scope

The row directions are deterministic, normalized and spanning. Selection is independent and identically distributed with strictly positive probabilities. **Noise is freshly resampled on every visit**, conditionally centered Gaussian with row-specific variance \(s_i>0\); the theorem is not about fixed once-for-all perturbations of a right-hand side. All Gaussian laws are real. The initial state is any deterministic vector, or more generally any independent state with finite fourth moment. There is no relaxation factor: each update is an exact orthogonal projection onto the newly observed noisy hyperplane.

## Proof

**1. Existence, uniqueness and moments.** Write \(P_i=I-u_i u_i^{\mathsf T}\), an orthogonal projector with norm at most one. Choose a finite word \(i_1,\ldots,i_\ell\) whose normal vectors span \(\mathbb R^d\). Then \(\|P_{i_\ell}\cdots P_{i_1}\|_2=\kappa<1\): equality at a unit vector would force each projector to preserve the norm at every stage; consequently every projector would leave that vector unchanged, making the vector orthogonal to all normals in the word, contradicting spanning. This word has positive probability \(\alpha\). For independent blocks of length \(\ell\) and every finite \(r\ge1\), the expected \(r\)-th power of the norm of a block product is at most \(1-\alpha(1-\kappa^r)<1\). Submultiplicativity yields exponentially decaying \(r\)-th moments of the norm of long products. In the two-sided stationary driving sequence, the pullback series consisting of all past Gaussian innovations transported through subsequent projector products therefore converges in \(L^r\) for every fixed finite \(r\), by Minkowski's inequality. Its law \(\pi\) is stationary. Coupling any two initial states with identical driving sequences makes their difference a product of the same projectors, converging to zero in \(L^r\); hence the stationary law is unique and is the limit from each specified initial state.

**2. Center and a Gaussian mixture rigidity lemma.** Stationarity implies \(\mathbb E X=\sum_i p_i P_i\mathbb E X\). Because \(\sum_i p_i u_i u_i^{\mathsf T}\) is positive definite by spanning, \(\mathbb E X=0\). Suppose \(\pi=N(0,S)\). Its one-step image is the finite mixture \(\sum_i p_i N(0,S_i)\), with \(S_i=P_iSP_i+s_i u_i u_i^{\mathsf T}\). For any real \(v\), comparing second and fourth moments of this mixture with those of \(N(0,S)\) gives

\[
\sum_i p_i v^{\mathsf T}S_i v=v^{\mathsf T}Sv,\qquad
\sum_i p_i(v^{\mathsf T}S_i v)^2=(v^{\mathsf T}Sv)^2.
\]

Their difference is the variance of the scalars \(v^{\mathsf T}S_i v\) under strictly positive weights, so it vanishes only if \(v^{\mathsf T}S_i v=v^{\mathsf T}Sv\) for every \(i\). Polarization gives \(S_i=S\) for all \(i\). This proof includes singular Gaussian components.

**3. Necessity of graph compatibility.** From \(S=P_iSP_i+s_i u_i u_i^{\mathsf T}\), multiplying by \(u_i\) gives \(Su_i=s_i u_i\). Since \(S\) is symmetric, eigenvectors belonging to unequal eigenvalues are orthogonal. Thus \(u_i^{\mathsf T}u_j\ne0\) forces \(s_i=s_j\), and transitivity forces constancy on every graph component.

**4. Sufficiency.** Distinct graph components have mutually orthogonal spans \(V_C\). Under constancy of \(s_i=s_C\) within each component define \(S_*:=\sum_C s_C\Pi_C\). Then \(S_*u_i=s_i u_i\) and, by symmetry, \(P_iS_*P_i+s_i u_i u_i^{\mathsf T}=S_*\). Every update therefore preserves \(N(0,S_*)\). Uniqueness from Step 1 proves that this is exactly \(\pi\). This also covers disconnected graphs and different noise levels between orthogonal components.

**5. Strict fourth cumulants and a lower bound.** Conditional on the entire past index sequence in the stationary pullback construction, \(X\) is centered Gaussian with some random finite positive-semidefinite covariance \(\Gamma\). For \(v\in\mathbb R^d\), write \(Z_v=v^{\mathsf T}\Gamma v\). Conditional Gaussian fourth moments give

\[
\operatorname{cum}_4(v^{\mathsf T}X)=3\operatorname{Var}(Z_v).
\]

Conditioning only on the latest chosen index \(I=i\) gives \(\mathbb E[Z_v\mid I=i]=v^{\mathsf T}S_i v\). The law of total variance yields the stated computable lower bound. If every direction had fourth cumulant zero, \(Z_v\) would be nonrandom for all vectors in the finite polarization-determining family \(\{e_j,e_j+e_k:j<k\}\), and hence \(\Gamma\) would be almost surely constant. The pullback law would be Gaussian, contrary to Step 3 whenever graph compatibility fails. Therefore some unit direction has a strictly positive fourth cumulant.

**Exact overdetermined example.** In \(\mathbb R^2\), take three rows \(u_1=(1,0)\), \(u_2=(0,1)\), \(u_3=(3/5,4/5)\), equal row probabilities \(1/3\), and row-noise variances \((1,1,4)\). The graph has edges \((1,3)\) and \((2,3)\) and is connected, so the invariant law cannot be Gaussian. The stationary covariance is exactly

\[
S=\begin{pmatrix}2405/1442&300/721\\300/721&1465/721\end{pmatrix}.
\]

Solving the finite fourth-moment recurrence gives the exact first-coordinate fourth cumulant

\[
\operatorname{cum}_4(X_1)=\frac{1489362309243}{1033030114564}>0.
\]

The lower bound in Step 5 already certifies \(\operatorname{cum}_4(X_1)\ge927369/1039682>0\). Exact rational computation is reproduced by `verify.py`. These exact finite recurrences certify this example, while Steps 1–5 prove the all-dimensional claim.

## Verification

The standalone standard-library Python program `verify.py` checks the graph witnesses, exact covariance and fourth-moment recurrences for the three-row example, and exact two-row Gaussian-mixture transition identities for multiple variances and sampling probabilities. It uses only rational arithmetic, includes assertions on the overdetermined example's covariance and fourth cumulant, and reports 140 successful assertions under Python 3. This is not an exhaustive enumeration of rows or dimensions; the universal conclusion relies on the analytic proof above.

## Relationship to prior work

Bergou–Boucherouite–Dutta–Li–Ma (arXiv:2308.16904, first submitted 2023-08-31) study randomized Kaczmarz with perturbed data and derive convergence/error-neighborhood bounds; their noisy vector is fixed for a run, whereas this theorem concerns newly sampled Gaussian row measurements and exact invariant-law Gaussianity. Agaskar–Wang–Lu (2014) analyze exact mean-square error and sampling probabilities, explicitly presenting the noise-free case; second-moment formulas do not imply a classification of invariant Gaussianity and positive fourth cumulants. Yoon–Klett–Feron (arXiv:1905.09427) bound covariance propagation for switching Gaussian-noise systems, without a nonorthogonality-graph characterization of exact stationary distributions. Chen–Ip (2014) show general scan-order dependence for incompatible Gibbs updates and a two-coordinate mixture theorem. This supplies relevant analogy, but their discrete-coordinate statements do not classify arbitrary overcomplete oblique row projections, and the present all-row graph characterization is not the two-coordinate mixture result. The elementary Gaussian-mixture rigidity and linear-algebra arguments used here are acknowledged rather than claimed individually as new.

## Limitations

The theorem assumes positive selection probabilities, unit spanning rows, independent fresh centered Gaussian innovations and full unit-relaxation Kaczmarz steps. It does not apply verbatim to noise drawn once and then frozen, non-Gaussian innovations, correlated index sequences, relaxed projections, or rank-deficient row families. The fourth-cumulant statement asserts strict positivity in some direction, not all directions or a universal numerical lower bound. An equivalent characterization in older specialized random affine-iteration or incompatible-Gibbs literature remains a publication-precedence risk; the comparisons are evidence of distinct scope, not proof of uniqueness.

## References

1. El Houcine Bergou, Soumia Boucherouite, Aritra Dutta, Xin Li, and Anna Ma, *A Note on Randomized Kaczmarz Algorithm for Solving Doubly-Noisy Linear Systems*, arXiv:2308.16904, first submitted 2023-08-31, https://arxiv.org/abs/2308.16904.
2. Ameya Agaskar, Chuang Wang, and Yue M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP 2014, https://doi.org/10.1109/GlobalSIP.2014.7032145.
3. Yongeun Yoon, Corbin Klett, and Eric Feron, *Bounding the State Covariance Matrix for a Randomly Switching Linear System with Noise*, arXiv:1905.09427, first submitted 2019-05-21, https://arxiv.org/abs/1905.09427.
4. Shyh-Huei Chen and Edward H. Ip, *Behavior of the Gibbs Sampler When Conditional Distributions Are Potentially Incompatible*, Journal of Statistical Computation and Simulation (2014), https://doi.org/10.1080/00949655.2014.968159.
