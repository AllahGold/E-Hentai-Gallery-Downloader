# A Very Simple E-Hentai Downloader
Just input the url of a starting page, and number of successive pages you want to download.
I wrote the thing in Spyder. It might need Anaconda environment to work, otherwise there might be SSL errors for getting HTTPS pages.

Detects the url of the image contained in a gallery page, download it, and then detects the url of next page, rinse and repeat. 
The program waits 1000-5000 milliseconds after reading a gallery page before starting to download the image, and will only retrieve the next page after the download is complete. It could be a little bit slow, but otherwise you might be detected for using program and get IP temporarily banned.

# 非常简陋的E-Hentai下载器
输入起始页的地址和要下载的页数即可。
在Spyder里写的，可能需要Anaconda环境运行，否则或因读取https的问题出现SSL错误。

打开本子里的一页，检测里面的图片地址，下载图片，然后检测出下一页地址，然后继续。
每读取一个页面，会等待1000-5000毫秒再开始下载图片，下载完毕再读取下一页。可能效率比较慢，但这样比较安全，E站会检测爬虫，检测到会暂时封禁IP。