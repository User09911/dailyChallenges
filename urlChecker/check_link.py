import urllib.request

all_links = ['https://drive.google.com/file/d/18FxaWk0jv694MxTRukjitQ4K63nVHX48/view', 'https://drive.google.com/file/d/1ObbJ03KJ3Xxs-VzG66XGzy93OU0ygyQd/view', 'https://drive.google.com/file/d/1k6KGMPSGisrDNDtw40wdxh4ZuwP0QW-5/view', 'https://drive.google.com/file/d/1tRP5rfZPCFWe9CCmYVL2SANFE-24eyxv/view', 'https://drive.google.com/file/d/1CTxuFnNS2y1NqzDNrWnmwChSX_W4Bz74/view', 'https://drive.google.com/file/d/1zqFRF76dYoFrwNPEElpisp4tkmBXCNgU/view', 'https://drive.google.com/file/d/1x2iW22GwekkRWjLaBSrhJn0M2t8Nr6k1/view', 'https://drive.google.com/file/d/1CQKmEjbMii297-xiJ8GDsh1qYtK55YDp/view',
             'https://drive.google.com/file/d/1-8NqTrw0WvNOJjO-OKTFatoI5-Xh0UOZ/view', 'https://drive.google.com/file/d/1ZQ6xDXDlMw5xZTm63sLqIk_JDCt46M6g/view', 'https://drive.google.com/file/d/1VcAG_pxAt9tPHWRMgBoI4fcH3HAYzSzy/view', 'https://drive.google.com/file/d/1xE4G_1OTNEvkTkwqDPCm7tMfUAOidKaf/view', 'https://drive.google.com/file/d/1Z7jfP1QBankoeuqGKUsorIY9Hm0b3Q_r/view', 'https://drive.google.com/file/d/1XqcZL_dlQ170KWt0NJPRa3kew9zaW1F8/view', 'https://drive.google.com/file/d/1u2Qqux7GiTqM69mYSooq7IV1zjq789jj/view', 'https://drive.google.com/file/d/10RDLi5LBZar_dAVAzEI65JRcID6BRj2d/view', 'https://drive.google.com/file/d/1PEQS9iclTPiIvVHIzHHT3gjwpg1RnFS_/view']

print("Checking links...\n")

for x in all_links:
    try:
        print(x + ": " + urllib.request.urlopen(x).getcode())
    except:
        print('link error')
