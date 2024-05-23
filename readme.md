# Scrapy Tutorial

This tutorial will guide you through the process of using Scrapy, a powerful web scraping framework, to extract data from websites.

## Prerequisites

Before getting started, make sure you have the following installed on your system:

- Python (version 3.9.7)
- Scrapy (version 2.11.2)

## Tutorial to Setup Scrapy :

1. Create virtual environment

```bash
python -m venv .venv
```

2. Activate (cmd) on windows

```bash
.venv\Scripts\Activate
```

3. Create Scrapy Porject

```bash
scrapy startproject somethinc
```

4. Change Directory

```bash
cd somethinc
```

5. Create spiders

```bash
scrapy genspider products
```

## Tutorial to Use Scrapy :

```bash
scrapy crawl products -o product.json
```
