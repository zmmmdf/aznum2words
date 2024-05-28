# AzNum2Words

- - -
![Davamlı İnteqrasiya](https://github.com/zmmmdf/aznum2words/actions/workflows/ci.yml/badge.svg?branch=master)
[![GitHub Stars](https://img.shields.io/github/stars/zmmmdf/aznum2words.svg?style=social&label=Stars&style=plastic)](https://github.com/zmmmdf/aznum2words/stargazers)
[![Lisenziya](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

[![Switch to English](https://img.shields.io/badge/lang-en-brightgreen)](./README.md)

## Məqsəd

AzNum2Words ədədləri Azərbaycan dilində sözlə ifadə etmə məqsədini daşıyır və bu, maliyyə əməliyyatları, hüquqi sənədlər və statistik analizlər kimi müxtəlif ehtiyacları qarşılayır.

## Quraşdırma

AzNum2Words kitabxanasını pip vasitəsilə quraşdıra bilərsiniz:

```bash
pip install aznum2words
```

## İstifadə

```python
from aznum2words import AzerbaijaniNumberConverter

converter = AzerbaijaniNumberConverter()
print(converter.convert(123456789))  # nəticə: bir yüz iyirmi üç milyon dörd yüz əlli altı min yeddi yüz səkkiz doqquz
```

## Testlər

AzNum2Words kitabxanası etibarlılığını və dəqiqliyini təmin etmək üçün geniş test əhatəsinə malikdir. Testləri icra etmək üçün pytest istifadə edə bilərsiniz:

```bash
pip install pytest
pytest
```

## Layihəyə Dəstək

AzNum2Words layihəsinə dəstək olmaq və töhfə vermək xoş qarşılanır! Töfhə vermək üçün aşağıdakı təlimatları izləyin:

1. Reponu fork edin.
2. Öz xüsusiyyətiniz üçün yeni bir branch yaradın (`git checkout -b feature/my-feature`).
3. Dəyişikliklərinizi commit edin (`git commit -am 'Yeni xüsusiyyət əlavə olundu'`).
4. Dəyişikliklərinizi branch-a push edin (`git push origin feature/my-feature`).
5. Dəyişikliklərinizi izah edən bir pull request yaradın.

## Töhfə verənlər

Bu layihəyə aşağıdakı şəxslər töhfə veriblər:

<!-- Contributors list -->
<a href="https://github.com/zmmmdf/aznum2words/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=zmmmdf/aznum2words" />
</a>

<!--Made with [contrib.rocks](https://contrib.rocks). -->
<!-- Contributors list -->
