# Pairwise independence of sliding-median changes at one window's separation

## Finding

Let \((X_i)_{i\in\mathbb Z}\) be iid real observations with an atomless common law. Fix a window width \(k\ge3\) and an **interior** rank \(2\le j\le k-1\), counted from the bottom. Let \(R_i\) be the \(j\)-th smallest observation among \(X_i,\ldots,X_{i+k-1}\), and write \(I_i=\mathbf1\{R_i\ne R_{i+1}\}\). Adjacent-window changes at starts separated by \(k\) depend on exactly one common input. If \(F_{j,k+1-j}\) is the \(\operatorname{Beta}(j,k+1-j)\) CDF and \(U\) is uniform on \([0,1]\), their covariance is exactly
\[
\operatorname{Cov}(I_i,I_{i+k})
=\frac{(k+1-2j)^2}{k^2}\operatorname{Var}\bigl(F_{j,k+1-j}(U)\bigr).
\]
In particular, the two indicators are independent if and only if \(k\) is odd and \(j=(k+1)/2\). At every other interior rank their covariance is strictly positive. For starts at distance \(d\ge k+1\), disjoint input sets already give pairwise independence. The median exception therefore occurs even when one input is shared.

## Proof

The probability integral transform gives iid uniform inputs and preserves their order almost surely: the original CDF is nondecreasing and the transformed variables have no ties. Use those uniform inputs and put \(S_i=1-I_i\). For starts \(0,k\), the determining inputs are \(X_0,\ldots,X_k\) and \(X_k,\ldots,X_{2k}\). Given \(X_k=x\) the two pairs of windows use independent remaining inputs. Time reversal shows that the two conditional retention probabilities coincide; denote them by \(h(x)\).

For either pair, write \(Z_1<\cdots<Z_{k-1}\) for the ordered inputs shared by the two adjacent windows within the pair. One window adds \(x\) to these inputs; the other adds a fresh uniform endpoint. A common selected value is \(Z_{j-1}\) if both endpoints are below \(Z_{j-1}\), or \(Z_j\) if both are above \(Z_j\). These are the only possibilities, since the common value must be a shared observation. Thus
\[
h(x)=\mathbb E\left[Z_{j-1}\mathbf1\{x<Z_{j-1}\}+(1-Z_j)\mathbf1\{x>Z_j\}\right].
\]
If \(f_\ell\) is the density of \(Z_\ell\), then
\[
h'(x)=-x f_{j-1}(x)+(1-x)f_j(x)
=\frac{k+1-2j}{k}\,F'_{j,k+1-j}(x).
\]
Indeed the two weighted densities on the left are respectively \((j-1)/k\) and \((k-j)/k\) times the \(\operatorname{Beta}(j,k+1-j)\) density. The boundary value \(h(0)=\mathbb E Z_{j-1}=(j-1)/k\) gives
\[
h(x)=\frac{j-1}{k}+\frac{k+1-2j}{k}F_{j,k+1-j}(x).
\]
Conditional independence gives \(\mathbb E[S_0 S_k]=\mathbb E[h(X_k)^2]\), while both marginal means are \(\mathbb E[h(X_k)]\). The covariance of the change indicators equals that of the retention indicators and hence is \(\operatorname{Var}(h(X_k))\). The beta density is positive throughout \((0,1)\), so this variance is strictly positive unless the CDF coefficient is zero. When it is zero the common conditional Bernoulli parameter is constant, so the unconditional joint law also factors. The argument applies at every start by stationarity.

## Relationship to prior work and scope

The cyclic sliding-maxima covariance law in *A negative-to-positive lag transition for cyclic sliding-window maxima* treats the extremal upper rank; the lower extremum follows by order reversal. Neither extremum is claimed here. *Universal rank laws and the endpoint-atom transition for sliding order-statistic plateaus* computes single-plateau laws and probabilities of consecutive equal outputs, which determine adjacent change covariance. Those formulas do not give the joint law of two separated retention events belonging to possibly different plateaus. The contribution here is the exact full-width covariance for interior ranks and the resulting median exception. Analog order-statistic output correlations (Bovik and Restrepo, 1987, doi:10.1016/0016-0032(87)90378-4) are a different statistic. Possible implicit coverage in older overlap or median-streak literature remains a limitation, in particular because the complete text of Bovik's *Streaking in median filtered images* (doi:10.1109/TASSP.1987.1165153) was not available for comparison.

Independence is pairwise, not a claim about the full sequence of change indicators. The theorem does not require a cyclic boundary and does not address intermediate lags, ties, or dependent observations.

## Verification

Run `python3 verify.py` to compare the stated covariance with exact exhaustive relative-order counts for widths three and four and every interior rank. The calculation integrates the beta-CDF polynomial exactly with rational arithmetic. It is a finite check; the conditional calculation above proves the general result.
