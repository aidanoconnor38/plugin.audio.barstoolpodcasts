import urllib, urllib2
import xbmcaddon, xbmcgui, xbmcplugin
import requests
from bs4 import BeautifulSoup


addon_handle = int(sys.argv[1])

podcasts = []
podcasts.append('Pardon My Take;http://is5.mzstatic.com/image/thumb/Music62/v4/b7/e4/67/b7e46778-c171-9c44-ba31-cf4'
                '2705467c7/source/600x600bb.jpg;http://podbay.fm/show/1089022756;On "Pardon My Take," Big Cat & PFT'
                ' Commenter deliver the loudest and most correct sports takes in the history of the spoken word. Dai'
                'ly topics, guests, and an inability to tell what the hosts might be doing will make this your new f'
                'avorite sports talk show. This is a podcast that will without a doubt change your life for the bett'
                'er- guaranteed, or your money back. *Pretend a reggaeton air horn is going off right now*')
podcasts.append('The Pat McAfee Show;http://is4.mzstatic.com/image/thumb/Music128/v4/d9/ba/3a/d9ba3a5c-b57e-e767-09'
                '23-06f08ad0b401/source/600x600bb.jpg;http://podbay.fm/show/1134713453;Everybody on earth is attempt'
                'ing to be the next podcast king... I am not. My name is Pat McAfee. I\'m an NFL punter/Comedian and'
                ' all I want to do is deliver folks a hilariously raw and adult conversation between my friends and I'
                '. Todd McComas, Shaun Latham, Chris Bowers and myself chat about life, sports, partying, and other '
                'reasons why America is majestically amazing. Thanks for listening. Cheers.')
podcasts.append('I am Rapaport;http://is4.mzstatic.com/image/thumb/Music117/v4/a8/4c/2f/a84c2f8b-dbab-c048-6dc6-c28'
                '11d049e22/source/600x600bb.jpg;http://podbay.fm/show/923017367;Actor/Director Michael Rapaport sha'
                'res his strong, funny & offensive points of view on life, sports, music, film & everything in betwe'
                'en on the I AM RAPAPORT: STEREO PODCAST.')
podcasts.append('Barstool Rundown;http://is3.mzstatic.com/image/thumb/Music62/v4/5b/30/5e/5b305ec3-fd5f-6991-9901-c'
                'c0754d99600/source/600x600bb.jpg;http://podbay.fm/show/1093320744;El Pres, KFC, and Big Cat and th'
                'e rest of Barstool Sports break down the biggest and funniest stories/videos from the internet that'
                ' day. The Rundown is the Front Page of the Internet in audio form, presented with a slant on men\'s'
                ' humor in a locker room atmosphere.')
podcasts.append('Barstool Radio;http://is5.mzstatic.com/image/thumb/Music122/v4/c3/5a/cc/c35acc45-7cfb-b19a-6f0a-89'
                'c791d58483/source/600x600bb.jpg;http://podbay.fm/show/1085919903;Introducing the Dave Portnoy Show'
                '. This show will focus on the inner workings of Barstool Sports. We\'ll talk about all the controve'
                'rsies, decisions and stories from the past that helped mold who we are today as well as questions that'
                ' will define the future. Basically an in-depth look behind the curtain of one of the most controversi'
                'al blogs on the planet and the guys who make it tick.')
podcasts.append('KFC Radio;http://is1.mzstatic.com/image/thumb/Music128/v4/bd/17/8e/bd178e3e-205c-67ef-1f2e-9bebc62'
                '9701f/source/600x600bb.jpg;http://podbay.fm/show/536209167;Featuring all of the regular Barstool per'
                'sonalities, KFC Radio is the quintessential bar conversation brought to podcast form. Listener intera'
                'ction is the name of the game as Barstool readers and listeners contribute their Stoolie Voicemails to'
                ' drive the conversation to strange places including embarrassing personal stories, bizarre hypotheti'
                'cal questions, and more. New episodes of the hilarious Barstool Network flagship show are released ev'
                'ery Friday.')
podcasts.append('Heartland Radio;http://is2.mzstatic.com/image/thumb/Music128/v4/5f/6a/51/5f6a513a-72e4-1ff3-783a-'
                'bbf424b61830/source/600x600bb.jpg;http://podbay.fm/show/1295887660;The supporting cast of The Pat M'
                'cAfee Show now have their own podcast. Come laugh with Todd McComas, Shaun Latham, Vibbs, Digs, Nick'
                ' Maraldo, and Ryan Cauley. Friends just hanging out, breaking balls, and discussing life as they k'
                'now it.')
podcasts.append('Fore Play;http://is3.mzstatic.com/image/thumb/Music122/v4/4e/33/90/4e3390d1-cc95-37a9-6665-2e93a1'
                'd0cdbd/source/600x600bb.jpg;http://podbay.fm/show/1200343264;"Fore Play" is a weekly podcast by com'
                'mon golfers, for common golfers. Trent, Riggs and their wide variety of guests talk about everything'
                ' golf like normal folks sitting at a bar watching coverage, venting about the game\'s difficulties, '
                'and weighing in on pro gossip. Your classic golf addicts, the "Fore Play" crew brings a young, uniq'
                'ue voice to the rapidly-evolving game, discussing freely and openly everything golf. There\'s nothing '
                'like it.')
podcasts.append('Laces Out;http://is3.mzstatic.com/image/thumb/Music128/v4/ee/5b/48/ee5b4877-ab6d-102b-0e3e-9cc546d'
                '5e693/source/600x600bb.jpg;http://podbay.fm/show/1277226274;Pat McAfee and AJ Hawk join Barstool Sp'
                'orts\' Jerry Thornton to answer the question, "What would it sound like if two NFL greats and a footb'
                'all writer got together to discuss everything in the NFL worth talking about and lots more stuff tha'
                't isn\'t?" If you listen to just one podcast for seriously insightful football analysis, you should al'
                'so listen to these guys sit around and mock everything.')
podcasts.append('The Podfathers;http://is3.mzstatic.com/image/thumb/Music118/v4/4e/2d/fa/4e2dfa02-0dea-556d-3f25-b'
                '31f34e10e0c/source/600x600bb.jpg;http://podbay.fm/show/1158624049;The Podfathers is a podcast from '
                'KFC, Clem and Uncle Chaps from Barstool Sports breaking down the good, the bad, and the ugly of fathe'
                'rhood. Other books and websites and podcasts have tried to explain what life as a new dad is like "fr'
                'om a dude\'s perspective." "As told by Guy\'s guys." or "from a mans perspective." They have all faile'
                'd. Through their own personal experiences and brand of humor, the Podfathers help parents everywhere '
                'relate to the wild and crazy ride that is raising children.')
podcasts.append('Barstool Pick Em;http://is4.mzstatic.com/image/thumb/Music128/v4/c2/0e/51/c20e5137-686c-8406-c228'
                '-4ffa5b001ff6/source/600x600bb.jpg;http://podbay.fm/show/1277969212;If you\'re looking for winners, '
                'you\'ve found the right place. Fade hosts Big Cat, Pres, and Rico Bosco as they give you all their '
                'losing picks with extreme confidence. Weekly talk about bad beats, close misses, and staring at the ce'
                'iling Sunday night thinking about how you\'ll pay your bookie. Rule number 1 of gambling, always bet '
                'the Over. Rule number 2, if a mascot dies the week of a big game, it\'s an automatic mortal lock.')
podcasts.append('Spittin Chiclets;http://is3.mzstatic.com/image/thumb/Music71/v4/92/dd/b7/92ddb7d6-109f-fb4a-33fb-'
                '6cb00326d312/source/600x600bb.jpg;http://podbay.fm/show/1112425552;The Boston Bruins writer at Bar'
                'stool Sports and former NHL defenseman talk hockey and also whatever else might come up on their ra'
                'dar.')
podcasts.append('Zero Blog Thirty;http://is5.mzstatic.com/image/thumb/Music111/v4/75/b8/b1/75b8b104-18bf-9c15-9ed4'
                '-eb2aadfac756/source/600x600bb.jpg;http://podbay.fm/show/1151856991;Uncle Chaps from BarstoolSports')
podcasts.append('Fantasy Football Follies;http://is2.mzstatic.com/image/thumb/Music128/v4/d5/b3/1a/d5b31a67-ced2-f9'
                'fe-9e09-6ccd91532d49/source/600x600bb.jpg;http://podbay.fm/show/1269607399;Every Thursday A.M. Acto'
                'r/Director/Fantasy Football Beast Michael Rapaport aka GM of RapaportsDelight aka There Will Be Blood'
                ' brings you the Fantasy Football Follies presented by DraftKings. Rapaport is bringing the personalit'
                'y to fantasy while delivering expert guests each week to speak on the fantasy and actual gridiron. Th'
                'is is the only podcast that lives by these bylaws: - There are NO friends in fantasy - Don\'t follow '
                'trends, set them - Go with your gut - Live to dominate the waiver wire - Win every draft - Know your '
                'guys, get your guys - Talk smack when you\'re winning, talk more smack when you\'re losing - Fly your'
                ' fantasy flag HIGH - Relish in doing your research - Yearn to be the MVP of Fantasy - Follow these and'
                ' you\'ll capture the Kings Crown in DFS & League Play Taking you all the way through the NFL Season, '
                'into your playoffs and to your own personal parade of confetti. Hoist the Lombardi in Fantasy and hav'
                'e fun along the way while showing no mercy. Smash that Subscribe button and come Dance with The Dingo.'
                ' Fantasy Football Follies, a Barstool Sports podcast')
podcasts.append('Starting 9;http://is5.mzstatic.com/image/thumb/Music118/v4/da/ea/16/daea167c-8cdf-fdec-4c96-90b55e'
                '901cfc/source/600x600bb.jpg;http://podbay.fm/show/1265632650;Barstool sports presents a baseball podc'
                'ast for fans of all parts of the game - on the field and off it. Hosted by former MLB pitcher Dallas '
                'Braden - owner of a perfect game - and Barstool baseball blogger Jared Carrabis, the Starting 9 is th'
                'e podcast for baseball conversations that are actually happening.')
podcasts.append('Failing Upwards;http://is4.mzstatic.com/image/thumb/Music118/v4/b2/cf/59/b2cf59b3-3f0e-dadb-2f7b-f'
                'f9ecd6c3122/source/600x600bb.jpg;http://podbay.fm/show/1124174033;Two grown dirtbags just trynna nav'
                'igate and survive the millennial male zeitgeist. If you have any money you\'d like to give us or any'
                ' constructive criticism you\'d like us to 360 degree tomahawk slam dunk into the trash can please em'
                'ail us: failingupwardspod@gmail.com.')
podcasts.append('From The Top Rope;http://is3.mzstatic.com/image/thumb/Music117/v4/2b/d3/f3/2bd3f3ee-e323-1fbf-e0c0'
                '-d8858429f965/source/600x600bb.jpg;http://www.podbay.fm/show/1247526507;The biggest stars in and aro'
                'und the professional wrestling business join hosts Robbie Fox and Jared Carrabis every Wednesday afte'
                'rnoon to dive into the biggest angles, news, and events of the week. Plus, bonus episodes every Monday'
                ' following a pay per view! Fox is the designer behind many of your favorite wrestler\'s ring attires '
                'and Carrabis is a lifelong fan, creating a unique dynamic you\'ll find on no other show!')
podcasts.append('Mickstape;http://is2.mzstatic.com/image/thumb/Music122/v4/1d/2a/15/1d2a15a2-0fd7-4f07-270a-3a98c93'
                'e07ad/source/600x600bb.jpg;http://podbay.fm/show/1166774961;Podcast by Coley Mick x Trill Withers')
podcasts.append('Section 10;http://is3.mzstatic.com/image/thumb/Music128/v4/51/f7/64/51f7647c-03d1-2949-afab-3f4bff'
                '6e1bd3/source/600x600bb.jpg;http://www.podbay.fm/show/976803232;')
podcasts.append('Yound & Happy;http://is2.mzstatic.com/image/thumb/Music111/v4/c2/39/f7/c239f7e8-19b9-a38a-e0f9-745'
                '0e749ec95/source/600x600bb.jpg;http://podbay.fm/show/1091764921;Thanks for listening to my podcast. I'
                ' don\'t have a strict plan for what it\'s going to be about. The only component I know that will rema'
                'in constant is me, so that\'s why I decided to just call it "The Caleb Pressley Show." It doesn\'t bo'
                'x us in. I will focus on things that I\'m interested in--whether that\'s food, sports, music, film, wh'
                'atever. I\'m going to grapple with some curious stuff, and my hope is that it is as mentally stimulat'
                'ing for y\'all as I know it will be for me.')


def getDOM(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')
    responce = urllib2.urlopen(req)
    returnDOM = responce.read()
    responce.close()
    return returnDOM

def removeListTags(item):
    return str(item).replace("'", '').replace('[', '').replace(']', '')

def listShows():
    list=[]
    for podcast in podcasts:
        podcast = podcast.split(';')
        query = urllib.urlencode({'mode': 'GE', 'url': podcast[2], 'image': podcast[1]})

        infoLabels = {'Title': podcast[0], 'FileName': podcast[0], 'Plot': '[B]' + podcast[0] + '[/B]\n' + podcast[3]}
        u = 'plugin://plugin.audio.barstoolpodcasts/?' + query

        li = xbmcgui.ListItem(podcast[0], iconImage=podcast[1])
        li.setInfo('video', infoLabels)
        li.setProperty('fanart_image', podcast[1])

        list.append((u, li, True))

    xbmcplugin.addDirectoryItems(addon_handle,list, len(list))
    xbmcplugin.endOfDirectory(addon_handle)

def getEpisodes(source, image):
    DOM = getDOM(source)
    soup = BeautifulSoup(DOM, 'html.parser')
    matches = soup.find_all('a', {'rel': 'tooltip'})

    list = []
    for match in matches:
        soup = BeautifulSoup(str(match), 'html.parser')
        link = soup.a['href']
        title = soup.a.string

        desc = soup.a['title'].replace('<p>', '').replace('</p>', '')
        desc = ''.join([i if ord(i) < 128 else ' ' for i in desc]).strip()
        infoLabels = {'Title': title, 'FileName': title, 'Plot' : '[B]' + title + '[/B]\n' + desc}

        query = urllib.urlencode({'mode': 'PE', 'url': link})
        u = 'plugin://plugin.audio.barstoolpodcasts/?' + query

        li = xbmcgui.ListItem(title, iconImage=image)
        li.setInfo('video', infoLabels)
        li.setProperty('IsPlayable', 'true')
        li.setProperty('fanart_image', image)

        list.append((u, li, False))

    xbmcplugin.addDirectoryItems(addon_handle, list, len(list))
    xbmcplugin.endOfDirectory(addon_handle)

def playEpisode(url):
    individualPage = getDOM(url=url)
    soup = BeautifulSoup(str(individualPage), 'html.parser')
    match = soup.find('a', {'class': 'btn btn-mini btn-primary'})
    xbmcplugin.setResolvedUrl(addon_handle, True, xbmcgui.ListItem(path=match['href']))

# MAIN EVENT PROCESSING STARTS HERE
# Query Handler
parms = {}
try:
    parms = dict(arg.split('=') for arg in ((sys.argv[2][1:]).split('&')))
    for key in parms:
      try:    parms[key] = urllib.unquote_plus(parms[key]).decode(UTF8)
      except: pass
except:
    parms = {}

p = parms.get
mode = p('mode',None)

if mode==  None:    listShows()
elif mode=='GE':    getEpisodes(urllib.unquote(p('url')), urllib.unquote(p('image')))
elif mode=='PE':    playEpisode(urllib.unquote(p('url')))
else:               xbmcgui.Dialog().ok('ERROR', 'Error: MODE not found!!!')

