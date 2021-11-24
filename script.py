code = f"""
<article>
 <a class="thumbnail" href="images/fulls/filename.jpg" data-position="left center"><img src="images/fulls/filename.jpg" alt="" /></a>
 <h2>Title</h2>
 <p>Description</p>
</article>
"""

for i in range(35):
    print(code.replace('filename', str(i+1)))