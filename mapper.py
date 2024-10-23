#takes a user, gives to reducer jk
#get all of the pairs of users and thier orders 
#!/Users/kassidywall/anaconda3/bin/python
import sys
import itertools
import json 
import nltk
from nltk.corpus import stopwords
import re
import contractions

nltk.download('stopwords')

sw = stopwords.words('english')


for line in sys.stdin:
    try:
        articles = json.loads(line)
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Error decoding JSON: {e} in line: {line}\n")
        continue
    
    for article in articles:
        url = article.get('url', article.get('page', None))
        if not url:
            sys.stderr.write(f"Error: Neither 'url' nor 'page' key found in article: {json.dumps(article)}\n")
            continue

        outlet = "ksl" if "ksl.com" in url else \
                 "cnbc" if "cnbc.com" in url else \
                 "verge" if "theverge.com" in url else "unknown"

    #articles = json.loads(line)

    #for article in articles:
        text = article.get('content', '').lower().strip()
        tokens = contractions.fix(text).split()
        cleaned_tokens = [re.sub(r'[^\w\s]', ' ', token).strip() for token in tokens if re.sub(r'[^\w\s]', ' ', token)]
        compacted_tokens = [word for word in cleaned_tokens if word.strip() ]
        filtered_tokens = [word for word in compacted_tokens if word not in sw]
        cleaned_text = ' '.join(filtered_tokens)
        kv = {"source": outlet, "content": cleaned_text}
        #print(f"{outlet}:::{cleaned_text}")
        print(json.dumps(kv))



'''for line in sys.stdin:
    try:
        articles = json.loads(line)
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Error decoding JSON: {e} in line: {line}\n")
        continue
    
    for article in articles:
        url = article.get('url', article.get('page', None))
        if not url:
            sys.stderr.write(f"Error: Neither 'url' nor 'page' key found in article: {json.dumps(article)}\n")
            continue

        outlet = "ksl" if "ksl.com" in url else \
                 "cnbc" if "cnbc.com" in url else \
                 "verge" if "theverge.com" in url else "unknown"

        text = article.get('content', '').lower().strip()
        tokens = contractions.fix(text).split()
        cleaned_tokens = [re.sub(r'[^\w\s]', ' ', token).strip() for token in tokens if re.sub(r'[^\w\s]', ' ', token)]
        compacted_tokens = [word for word in cleaned_tokens if word.strip()]
        filtered_tokens = [word for word in compacted_tokens if word not in sw]
        cleaned_text = ' '.join(filtered_tokens)

        print(f"{outlet}:::{cleaned_text}")'''


'''for line in sys.stdin:
    line = line.strip() 
    if not line:
        continue
    #try:
        #articles = json.loads(line)
    #except json.JSONDecodeError:
        #continue

    articles = json.loads(line)
    
    for article in articles:
        url = article.get("url") or article.get("link")
        outlet = extract_outlet(url)
        
        text = article['content'].lower().strip()
        tokens = contractions.fix(text).split()
        cleaned_tokens = [re.sub(r'[^\w\s]', ' ', token).strip() for token in tokens if re.sub(r'[^\w\s]', ' ', token)]
        compacted_tokens = [word for word in cleaned_tokens if word.strip()]
        filtered_tokens = [word for word in compacted_tokens if word not in sw]
        cleaned_text = ' '.join(filtered_tokens)

        print(f"{outlet}:::{cleaned_text}")'''





'''for line in sys.stdin:
    articles = json.loads(line)
    for article in articles:
        text = article['content'].lower().strip()
        tokens = contractions.fix(text).split()
        cleaned_tokens = [re.sub(r'[^\w\s]', ' ', token).strip() for token in tokens if re.sub(r'[^\w\s]', ' ', token)]
        compacted_tokens = [word for word in cleaned_tokens if word.strip() ]
        filtered_tokens = [word for word in compacted_tokens if word not in sw]
        #text = ' '.join([word for word in text.split() if word not in sw])
        #filtered_tokens = [re.sub()]
        text = ' '.join(filtered_tokens)
        print(f"{article['url']}:::{text}")'''
















'''shingle_size = 3

#lines = sys.stdin

for line in sys.stdin:
    #print(line)
    perms = itertools.permutations(line.split(), shingle_size)
    
    for perm1 in perms:
        for perm2 in perms:
            pairing = {'1': list(perm1), '2': list(perm2)}
            print(json.dumps(pairing))
            #print(' '. join(perm))


#should create the shinlges '''

'''for line in sys.stdin:
    if line[0] == 'e':
        continue
    values = line.strip().split('')
    user_id = values[-1]

    product_id = values[2]
    print(f"{user_id}, {product_id}")'''



    
