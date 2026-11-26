# Sharp arm-dominance transition for resistance-diameter design on spider trees

## Finding

Let a spider tree have a center and \(m\ge 2\) internally disjoint nonempty paths (arms) from the center to distinct leaves. For arm \(i\), let \(E_i\) denote its edge set; each edge \(e\) has an arbitrary positive price \(p_e\) per unit of electrical conductance. Choose every edge conductance \(w_e>0\) independently, with total cost \(\sum_e p_e w_e\le B\), where \(B>0\). The objective is the **resistance diameter** \(D(w)=\max_{u,v}R_{uv}(w)\), the maximum effective resistance over all vertex pairs.

Put
\[
s_i=\sum_{e\in E_i}\sqrt{p_e},\qquad C=\sum_{i=1}^m s_i^2,
\qquad j\in\operatorname*{argmax}_i s_i,\qquad U=C-s_j^2>0.
\]
The unique global minimum and the unique optimal conductances have exactly two regimes.

**Balanced arms, \(s_j^2\le U\):**
\[
D_*=\frac{2C}{B},\qquad
w_e^*=\frac{B s_i}{C\sqrt{p_e}}\quad(e\in E_i).
\]
All optimal arm resistance totals are equal to \(C/B\).

**Dominant arm, \(s_j^2>U\):**
\[
D_*=\frac{(s_j+\sqrt U)^2}{B},\qquad
w_e^*=\begin{cases}
\dfrac{B}{(s_j+\sqrt U)\sqrt{p_e}},&e\in E_j,\\[2mm]
\dfrac{B s_i}{\sqrt U(s_j+\sqrt U)\sqrt{p_e}},&e\in E_i,\ i\ne j.
\end{cases}
\]
The distinguished arm has resistance \(s_j(s_j+\sqrt U)/B\); all others have the common resistance \(\sqrt U(s_j+\sqrt U)/B\). The two formulas agree at equality in the threshold. Since \(m\ge2\) and every \(s_i>0\), a strictly dominant index is unique.

In particular, if all edge prices equal one, \(s_i=|E_i|\), and the transition occurs precisely when the **square of the longest arm length** exceeds the sum of the squared lengths of all other arms.

## Assumptions and scope

The graph is a finite undirected tree with exactly one possible branch center; each arm is a simple nonempty path and different arms intersect only at the center. The number and lengths of arms are unrestricted except \(m\ge2\); prices and budget are arbitrary positive real numbers. Conductances must be strictly positive so all resistance distances are finite. Effective resistance is defined by unit current injection and extraction, and the resistance of a tree path is the sum of reciprocal edge conductances. The maximum includes every pair of vertices, not just leaf pairs. The budget is an inequality, but it is saturated at the optimum.

## Proof

**1. Diameter reduction.** For arm \(i\) set \(R_i=\sum_{e\in E_i}w_e^{-1}\). Every vertex-to-vertex tree resistance is a subpath sum. Since all terms are positive, the resistance diameter is attained by two leaves on different arms, and
\[
D(w)=\max_{1\le i<k\le m}(R_i+R_k).
\]
A pair on one arm or with the center cannot exceed the sum of the two largest \(R_i\).

**2. Sharp within-arm cost.** Cauchy--Schwarz gives, for each arm,
\[
\left(\sum_{e\in E_i}p_e w_e\right)
\left(\sum_{e\in E_i}w_e^{-1}\right)
\ge \left(\sum_{e\in E_i}\sqrt{p_e}\right)^2=s_i^2.
\]
For prescribed \(R_i>0\), the least arm cost is \(s_i^2/R_i\), with equality *only* at \(w_e=s_i/(R_i\sqrt{p_e})\). Thus the original problem reduces exactly, including equality and uniqueness, to minimizing \(\max_{i<k}(R_i+R_k)\) with \(\sum_i s_i^2/R_i\le B\).

**3. Fixed-diameter cost.** Fix \(D>0\). Minimize \(\sum_i s_i^2/R_i\) over positive arm resistances satisfying \(R_i+R_k\le D\) for all \(i\ne k\). Order them \(R_{(1)}\ge R_{(2)}\ge\cdots\). Increasing any \(R_{(i)}<R_{(2)}\), \(i\ge3\), to \(R_{(2)}\) maintains all pair constraints and strictly decreases cost. The maximum pair must equal \(D\), since otherwise scaling every resistance upward would strictly decrease cost. Therefore at the minimum one arm has value \(xD\), all other arms have value \((1-x)D\), with \(1/2\le x<1\). If the first value is larger, a cost-reducing interchange argument assigns it to a largest \(s_i^2\); at equality the assignment is immaterial. Consequently the minimum required budget is
\[
\frac1D\min_{1/2\le x<1}
\left(\frac{s_j^2}{x}+\frac{U}{1-x}\right).
\]
The bracketed function is strictly convex and has unconstrained minimizer \(x_0=s_j/(s_j+\sqrt U)\). If \(s_j^2\le U\), its constrained minimizer is \(x=1/2\) and the minimum is \(2C\). Otherwise \(x=x_0\) and the minimum is \((s_j+\sqrt U)^2\).

**4. Optimal value and rigidity.** A feasible design of diameter \(D\) must therefore satisfy \(B\ge F/D\), where \(F\) is the relevant value in step 3. Hence \(D\ge F/B\). The displayed conductances attain the bound and exhaust the budget. Strict convexity in the one-parameter reduction, strict improvement when an inferior arm resistance differs, and the equality case in Cauchy--Schwarz force exactly the displayed positive conductances. Thus the optimizer is unique, including at the regime boundary.

## Verification

The standalone `verify.py` uses exact rational arithmetic on balanced and dominant integer-arm examples, verifies every budget and predicted resistance-diameter identity, checks independent feasible conductance allocations against the analytic lower bound, and calculates full-vertex diameters directly on generated trees. Its run reports **13,714 successful assertions**. An optional `optcheck.py` uses SciPy's independently formulated epigraph nonlinear optimization: all 20 objective values agree with the formula within \(10^{-7}\); 16 runs report successful optimizer termination and four stop with a line-search flag despite comparable objective values. Neither finite experiment substitutes for the universal proof above.

As a nondegenerate equal-price example, three arms of respective lengths \(4,1,1\) and budget \(B\) satisfy \(s_j^2=16>2=U\). The optimum is \((4+\sqrt2)^2/B\), whereas uniform per-edge conductance gives diameter \(30/B\).

Run `python3 verify.py`; optionally run `python3 optcheck.py` with NumPy and SciPy installed.

## Relationship to prior work

Ghosh, Boyd and Saberi (2006) formulate and analyze convex edge-conductance allocation for **total** effective resistance; their Section VII explicitly observes that minimizing the **maximum** effective resistance is also a convex problem representable by an SDP. That general framework is prior art, not claimed here. The present statement supplies a specialized closed form for every spider topology, arbitrary edgewise prices, the unique *individual-edge* allocation, and a necessary-and-sufficient arm-dominance threshold. These are not the total-resistance solution or a formula printed in the inspected Section VII.

Roos, Bai and Chaerani (2012) treat robust resistor-network design with single-current and multi-current semidefinite models. Their inspected modeling and examples do not state a spider-tree resistance-diameter classification. A general numerical conic formulation can evaluate the design instance but does not, without solving the specific structural minimax, imply the displayed threshold. Earlier analytical results about two-hub double stars address a different graph family and do not subsume the one-hub multiedge-arm classification.

## Limitations

The result does not classify general trees with multiple branching vertices, networks with cycles, edge capacity caps, nonlinear prices, or objective functions other than maximum pairwise effective resistance. A general conic solver can attack broader classes; this theorem instead gives a closed-form specialized solution. No independent mathematical audit has been performed. Bibliographic search and primary-source inspection reduce but cannot eliminate the risk of an unlocated equivalent specialized proof.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, Kyoto, pp. 1185--1196, July 24--28, 2006. Full proceedings version: https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf . Journal version: *SIAM Review* 50 (2008), 37--66, https://doi.org/10.1137/050645452 .
2. C. Roos, Y. Bai and D. Chaerani, *Robust Resistance Network Topology Design by Conic Optimization*, *Sultan Qaboos University Journal for Science* 17 (2012), 125--146, https://doi.org/10.24200/squjs.vol17iss1pp125-146 .
