# Independent mathematical audit

## correctness

PASS

PASS: On each finite Dirichlet m-grid the eigenvalues are 4m²sin²(jπ/(2m)), λ_min≥4 and λ_max=4m²cos²(π/(2m)). In one mode, θ-step factor r=[1−(1−θ)λk]/[1+θλk], control coefficient p=k/(1+θλk) and weighted discrete cost kΣ|u_i|² yield Wθ= (1−r^{2N})/[λ(2+(2θ−1)λk)]. The continuous semidiscrete Gramian is (1−exp(−2λT))/(2λ). Their ratio is exactly 2/(2+α λk) × (1−r^{2N})/(1−exp(−2λT)). Two bounds B1=sup αλ_max k and B2=sup λ_max k² give a positive uniform ratio by r^{2N}≤exp[−N(1−r²)] and λ_min≥4; unbounded B1 or B2 produces high-frequency modal ratio tending to zero. With a=αλ_max k→a∞ and b=λ_max k²→b∞, r→−1 and N log r²→−4T(2+a)/b if b>0, giving the stated exact profile; b=0 gives 2/(2+a). Independently checked 240 finite modal Gramian examples. No infinite-family inference from those samples.

## originality

PASS

Best-of-knowledge original: exact finite-horizon fully distributed control Gramian and sharp necessity/sufficiency across simultaneous spatial/time refinement, plus the two-dimensional high-frequency critical ratio, are not established by relevant reviewed boundary-control and general numerical-control works; possible inaccessible classical coverage is expressly reserved.

## value

PASS

PASS: The natural question is whether numerical terminal energy remains uniformly comparable to exact continuous-time energy simultaneously across all spatial frequencies; the sharp two-parameter mesh threshold distinguishes Crank–Nicolson's k~h from the k~h² requirement for fixed θ>1/2. The high-frequency boundary profile is a nontrivial exact quantitative result, not an arbitrary slice or mere reparameterization, with direct implications for selecting fully-actuated discrete control meshes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
