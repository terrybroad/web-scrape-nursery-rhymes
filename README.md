# Web Scrape Nursery Rhymes Dataset
Web scraping code for building dataset of nursery rhymes from the website [allnurseryrhymes.com](https::/allnurseryrhymes.com)

The dataset can be found at: https://github.com/terrybroad/nursery-rhymes-dataset

## Requirements:
- `scrapy`
- `beautifulsoup4`

## How to run:

**Step 1: Crawl allnurseryrhymes.com**

We will use scrapy to crawl every page on all [allnurseryrhymes.com](https::/allnurseryrhymes.com) and extract the page contents. The 'spider' which is the code that does the crawling for this site can be found at `nursery_rhymes_project/spiders/nursery_rhymes_spider.py`

To crawl the site and extract the contents of every page run:

`scrapy crawl nursery_rhymes_spider -o output.json`

This will will give us a file called `output.json` with our web data in.

**Step 2: Filter output**

The next stage is to filter out pages that are not nursery rhymes. To do this we will look at the URLs and check the path to the page (the bit following the `.com`). If it matches one of the cases we have put in our [regex](https://regex101.com/) we will filter it out of the dataset. 

To run the code, run the command:
`python filter_output.py`

We will now have a file called `output_filtered.json` which should only contain page information of pages that are nursery rhymes.

**Step 3: Extract text**

We now want to extract the text of the nursery rhyme from the contents of the page. To do this we use the library beatiful soup for parsing the html and finding the contents we want, and regex to find keywords. Each page is different and this does not work perfectly every time, but most pages have the lyrics under a heading which usually ends with either the words 'Lyrics' or 'Translation'. And we capture all of the text after the last of these. If we cannot find headings with these words, we resort to capturing the text after the last heading tag.

To run this code, run the command:
`python extract_lyrics.py`

We should now have a folder called lyrics, with each of our nursery rhymes in as a text file. 


**Step 4: Analyse the data**

Now it is time to check the data. As stated earlier, websites are messy and webscraping will never be 100% perfect. Some of these will have multiple languages in, some will have additional unwanted text, and some will not have extracted all of the lyrics. We will have to go through them one by one if we want to make sure our dataset is perfect. 

*Tip:* the file name is the same as the path of the url, to check the page just append the file name to the URL [allnurseryrhymes.com](https::/allnurseryrhymes.com), i.e. the URL for `the-wheels-on-the-bus.txt` is [allnurseryrhymes.com/wheels-on-the-bus](https::/allnurseryrhymes.com/the-wheels-on-the-bus) 
