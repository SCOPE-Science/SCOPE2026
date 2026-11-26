# Independent mathematical audit

## correctness

PASS

The eight-state chain is irreducible (the positive-rate ordinary boundary and hop moves alone let every occupancy pattern reach and be reached from empty). A simple eigenvalue at 0 with spectral gap gives linear cumulant growth for any start: near s=0, log E exp(sN(t)) = tλ(s)+O(1) with bounded derivatives, since the leading analytic projection is nonzero at s=0. Tilting only the off-diagonal marked rates counts successful jumps and leaves the escape diagonal unchanged. Differentiating the normalized right eigenvector yields the stated centered Poisson equation and λ″(0)=j+2·1ᵀJr. Each boundary–bond count difference is a bounded occupancy change; with O(t) count variance the associated covariance is O(sqrt(t)), so both variance rates and both means agree. The independent replay /workspace/replays/3.py computes the characteristic determinant det(λI−Q_mark(z)) with jump multiplier 1+z and no linear solve; each low-total-degree coefficient has u-degree at most four (only four rows vary). Five exact integer evaluations suffice to recover each coefficient; write its Taylor terms Aλ+Bz+Dλ²+Eλz+Gz², giving j=−B/A and F=1−2(Dj²+Ej+G)/(Aj) after z=exp(s)−1. All exact mean, Fano and derivative ratios match. Exact positive denominator and numerator variations are 0,1,1,2; the stated sign tests at 0,3 and 0,1/4,1 attain the root-count bounds, counting multiplicities, so all positive roots are simple. Independent endpoint limits and opposite signs in all four rational root brackets match. The desorption upper turning point is a strict local maximum, not a global maximum (the far endpoint limit is 1); the shape classification and turning-point wording are read in that local sense. The count floors, endpoint singularity of the adsorption mean at u=0, and finite- versus long-time observables are correctly separated.

## originality

PASS

No earlier equivalent four-channel fixed-unit-desorption critical-point classification was identified in these bounded comparisons. The exact count-statistics calculation on this parameter path, not the TASEP–Langmuir model, eigenvalue method or an arbitrary finite-state formula, is the defensible contribution.

## value

PASS

Three is the smallest open chain having a genuine bulk exchange site with separately identifiable entrance, exit, adsorption and desorption statistics. A global certificate on the natural experiment of changing attachment alone distinguishes three qualitatively different shapes and gives two simple stationary points for detachment while proving no missed turns. It is a useful exact check for finite-state counting calculations or approximations, not a claim of a large physical noise excursion; the desorption swing is about 0.006 and long-time/three-site/unit-rate scope matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
