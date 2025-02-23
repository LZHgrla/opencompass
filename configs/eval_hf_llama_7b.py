from mmengine.config import read_base

with read_base():
    from .datasets.collections.base_medium_llama import piqa_datasets, siqa_datasets
    from .models.hf_llama_7b import models


datasets = [*piqa_datasets, *siqa_datasets]
