# Independent mathematical audit

## correctness

PASS

For b=Uᵀ(x−p₀), the normal equation on an edge in direction i gives foot coordinate (bᵢ−Σgᵢⱼεⱼ)/gᵢᵢ. Maximizing the left endpoint and minimizing the right endpoint independently over the fixed binary coordinates gives precisely (Lᵢ,Hᵢ). Center the coordinates at 1/2: set y=b−G1/2. The edge conditions are |yᵢ|<δᵢ/2. On a face with free indices I, let zᵢ=yᵢ−Σ_{j∉I}gᵢⱼ(εⱼ−1/2); then |zᵢ|<(gᵢᵢ−Σ_{j∈I,j≠i}|gᵢⱼ|)/2. The affine Jacobi map tᵢ↦(zᵢ−Σ_{j∈I,j≠i}gᵢⱼtⱼ)/gᵢᵢ maps the closed centered half-cube strictly into its interior and is a sup-norm contraction by strict dominance. Its unique fixed point is the centered projection foot. I=[d] gives interiority; vertices are automatic. Nonpositive δᵢ makes the strict edge interval empty, including equality. The image box is centered at p₀+U1/2 with volume ratio ∏δᵢ/det G. The equiangular determinant (1−c)²(1+2c) gives both stated rational examples and the c=1/2 failure.

## originality

PASS

The all-face kernel is prior, and the edge-strip characterization in the plane is already given by Pavlík. The distinct result here is the arbitrary-dimensional edge sufficiency for skew parallelotopes, with the Gram box, exact row-dominance threshold and determinant probability. In the checked prior results none provides those higher-dimensional conclusions or an evaluated formula that subsumes them.

## value

PASS

The result classifies admissible centers for a natural all-dimensional family, including arbitrary mixed signs and unequal generator lengths. It replaces a growing set of face checks by 2d sharp scalar inequalities and gives the exact uniform probability as the center set collapses at the shear threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
