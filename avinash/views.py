from django.shortcuts import HttpResponse

def navigation(request):
    s = '''<h2>STATUS ZONE AVINASH<br></h2>
            <a href="https://www.youtube.com/channel/UC_rnEu1W9eCHH5OdWZGuzKg">YOUTUBE</a><br> 
            <a href="https://www.instagram.com/avinash_gupta1999/">INSTAGRAM</a><br>
            <a href="https://chat.whatsapp.com/DbLjQraoZFx7gQBwvpnE4O">WHATAAP</a><br>
            <a href="https://knowledgeofavinash.blogspot.com/2020/09/pubg-ban-why.html?spref=tw&m=1">BLOG</a><br>
            <a href="https://www.facebook.com/profile.php?id=100016490114491">FACEBOOK</a>'''
    return HttpResponse(s)