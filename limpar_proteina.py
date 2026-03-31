from Bio.PDB import PDBParser, PDBIO, Select

class AminoAcidSelect(Select):
    def accept_residue(self, residue):
        # Aceita apenas resíduos que não são água (HOH) ou heteroátomos
        return residue.get_resname() not in ["HOH", "WAT"]

parser = PDBParser(QUIET=True)
estrutura = parser.get_structure("TNF", "1TNF.pdb")

io = PDBIO()
io.set_structure(estrutura)
io.save("1TNF_limpo.pdb", AminoAcidSelect())

print("Sucesso! Proteína limpa e salva como: 1TNF_limpo.pdb")
