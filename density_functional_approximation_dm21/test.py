import density_functional_approximation_dm21 as dm21
from pyscf import gto
from pyscf import dft
from time import time

# Create the molecule of interest and select the basis set.
mol = gto.Mole()
mol.atom = 'Si 0.0 0.0 0.0'
mol.basis = 'cc-pVDZ'
# mol.spin = 1
mol.build()

# Create a DFT solver and select the exchange-correlation functional.
mf = dft.UKS(mol)
# mf.xc = 'b3lyp'
mf._numint = dm21.NeuralNumInt(dm21.Functional.DM21)

# Run the DFT calculation.
start = time()
mf.kernel()
print(mf.get_fock().shape)
print("time ellapse: {:.2f}s".format(time() - start))