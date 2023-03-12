# Anime Image Captioning using OFA

This repo simply using pretrained weight of caption data in OFA repo to generate caption for anime face images

## Environments

- Python 3.10.9

Install libraries

``` bash
pip install -r requirements.txt
```

## Prepare

### Pretrained weight

In this project, I used [Finetuned base checkpoint for Caption on COCO]() in [checkpoints.md](./checkpoints.md), you can use any model of your choice

### Input file

Tutorial [here](https://github.com/OFA-Sys/OFA#image-captioning). Input file in `.tsv` format with uniq-id, image-id, caption, predicted object labels (taken from VinVL, not used), image base64 string are separated by tabs.

```
162365  12455   the sun sets over the trees beyond some docks.  sky&&water&&dock&&pole  /9j/4AAQSkZJ....UCP/2Q==
```

Convert to `.tsv` format with `./scripts/img2base64.py`

And you will obtain `.tsv` file

## Infer

You can modify path in `./tools/evaluate_caption_custom.sh` and run

``` bash
bash ./tools/evaluate_caption_custom.sh
```

## Result

Example results

| Image | Caption |
|:---:|:---:|
| ![image](./assets/000000.jpg "image") | a girl with long blonde hair wearing a bow tie |

## Citation

```
@article{wang2022ofa,
  author    = {Peng Wang and
               An Yang and
               Rui Men and
               Junyang Lin and
               Shuai Bai and
               Zhikang Li andv
               Jianxin Ma and
               Chang Zhou and
               Jingren Zhou and
               Hongxia Yang},
  title     = {OFA: Unifying Architectures, Tasks, and Modalities Through a Simple Sequence-to-Sequence
               Learning Framework},
  journal   = {CoRR},
  volume    = {abs/2202.03052},
  year      = {2022}
}
```

## Acknowledgement

This repo builds on the codebase of [OFA](https://github.com/OFA-Sys/OFA)

## ORIGINAL README FILE [HERE](./original_README.md)