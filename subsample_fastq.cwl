cwlVersion: v1.0
class: CommandLineTool

baseCommand: python

inputs:
  r1:
    type: File
    inputBinding:
      position: 1
  r2:
    type: File
    inputBinding:
      position: 2
  threshold:
    type: int
    default: 120000000
    inputBinding:
      prefix: "--threshold"
  seed:
    type: int
    default: 11
    inputBinding:
      prefix: "--seed"
  output_prefix:
    type: string
    default: "subsampled"
    inputBinding:
      prefix: "--output-prefix"
  output_dir:
    type: Directory
    default: /data
    inputBinding:
      prefix: "--output-dir"

outputs:
  r1_output:
    type: File
    outputBinding:
      glob: "$(inputs.output_dir)/${inputs.output_prefix}_$(basename ${inputs.r1})*.gz"
  r2_output:
    type: File
    outputBinding:
      glob: "$(inputs.output_dir)/${inputs.output_prefix}_$(basename ${inputs.r2})*.gz"

# Docker requirements
requirements:
  - class: ResourceRequirement
       ramMin: 48000
       coresMin: 4
  - class: DockerRequirement
    dockerPull: ghcr.io/msk-access/subsample_fastq:0.0.1
'dct:contributor':
  - class: 'foaf:Organization'
    'foaf:member':
      - class: 'foaf:Person'
        'foaf:mbox': 'mailto:shahr2@mskcc.org'
        'foaf:name': Ronak Shah
    'foaf:name': Memorial Sloan Kettering Cancer Center
'dct:creator':
  - class: 'foaf:Organization'
    'foaf:member':
      - class: 'foaf:Person'
        'foaf:mbox': 'mailto:shahr2@mskcc.org'
        'foaf:name': Ronak Shah
    'foaf:name': Memorial Sloan Kettering Cancer Center
'doap:release':
  - class: 'doap:Version'
    'doap:name': merge_fastq
    'doap:revision': 0.1.1