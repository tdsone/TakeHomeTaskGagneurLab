from mmsplice.vcf_dataloader import SplicingVCFDataloader
from mmsplice import MMSplice, predict_save


# files
gtf = 'data/chr1.gtf.gz'
fasta = 'data/chr1.fa'

vcf_benign = 'data/clinvar_chr1_benign.vcf.gz'
vcf_pathog = 'data/clinvar_chr1_pathogenic.vcf.gz'

pred_benign = 'pred_benign.csv'
pred_pathogen = 'pred_pathogen.csv'

dl_benign = SplicingVCFDataloader(
    gtf, fasta, vcf_benign, tissue_specific=False)
dl_pathogen = SplicingVCFDataloader(
    gtf, fasta, vcf_pathog, tissue_specific=False)


model = MMSplice()

predict_save(model, dl_benign, output_csv=pred_benign,
             pathogenicity=True, splicing_efficiency=True)

predict_save(model, dl_pathogen, output_csv=pred_pathogen,
             pathogenicity=True, splicing_efficiency=True)
