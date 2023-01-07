import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AninX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from random import choice
from AninX import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from AninX.misc import SUDOERS
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()





rodod = [
"من محبّين الليل أو الصبح؟ ",   
"‏- كتاب تقرأه هذه الأيام؟",   
"‏- نسبة رضاك عن تصرفات مَن تعرفهم في الفترة الأخيرة؟",   
"‏- اكتشفت أن الشخص المقرّب أخبر أصدقائك بِسر مهم عنك، ردة فعلك؟👀",   
"‏- شخص يقول لك تصرفاتك لا تعجبني غيّرها، لكن أنت ترى أن تصرفاتك عادية، ماذا تفعل؟",   
"حالياً الاغنية المترأسة قلبك هي؟",   
"‏- أقوى عقاب بتسويه لشخص مقرّب اتجاهك؟",   
"‏- هل تُظهِر حزنك واستيائك من شخص للآخرين أم تفضّل مواجهته في وقتٍ لاحق؟",   
"‏- أكلة يُحبها جميع أفراد المنزل ما عدا انت؟",   
" مين افخم بوت في التيلجرام?",   
" ‏- اكتشفت أن الشخص الذي أحببته يتسلى بك لملئ فراغه، موقفك؟",   
"‏- تاريخ جميل لا تنساه؟",   
"لو اتيحت لك فرصة لمسح ذكرى من ذاكرتك ماهي هذه الذكرى؟",  
" -  من علامات الجمال وتعجبك بقوة؟",   
" -  يومي ضاع على ....؟",   
" -  أكثر شيء تقدِّره في الصـداقات؟",   
" -  صفة تُجمّل الشخـص برأيك؟",   
" -  كلمة غريبة من لهجتك ومعناها؟",   
" -  شيء تتميز فيه عن الآخرين؟",   
" -  ‏وش أول جهاز جوال اشتريته ؟؟",   
" -  ‏وش اول برنامج تفتحه لما تصحى من النوم وتمسك جوالك ؟",   
" -  ‏كلما ازدادت ثقافة المرء ازداد بؤسه, تتفق؟",   
" -  ‏برايك من أهم مخترع المكيف ولا مخترع النت ؟",   
" -  ‏وش رايك بالزواج المبكر ؟",   
" -  ‏وش أكثر صفه ماتحبها بشخصيتك  ؟",   
" -  ‏من اللي يجب ان يبادر بالحب اول البنت لو الولد؟",   
" -  ‏هل تعايشت مع الوضع الى الان او لا؟",   
" -  ‏كيفك مع العناد؟",   
" -  ‏هل ممكن الكره يتبدل؟",   
" -  ‏بشنو راح ترد اذا شخص استفزك؟",   
" -  ‏كم زدت او نقصت وزن في الفتره ذي؟",   
" -  ‏تشوف في فرق بين الجرأة والوقاحة؟",   
" -  ‏اكثر مدة م نمت فيها؟",   
" -  ‏اغلب قراراتك الصح تكون من قلبك وله عقلك؟",   
" -  ‏كم تريد يكون طول شريكك؟",   
" -  ‏لو فونك بيد احد اكثر برنامج م تبيه يدخله هو؟",   
" -  ‏اعظم نعمة من نعم الله عندك؟.",   
" -  ‏اغلب فلوسك تروح على وش؟",   
" -  ‏رايك بالناس اللي تحكم ع الشخص من قبيلته؟.",   
" -  ‏اكثر اسم تحب ينادوك فيه؟",   
" -  كم من مية تحب تشوف مباريات؟",   
" -  ‏اكثر شي مع اهل امك وله ابوك؟",   
" -  ‏صراحةً شكل الشخص يهم اذا انت بتحب شخص؟",   
" -  ‏فراق الصديق ام فراق الحبيب ايهم اسوء؟",   
" -  مين أعظم وأفخم بوت في التيلي؟",   
" -  كم لغة تتقن؟",   
" -  وش اجمل لغة برأيك؟",   
" -  تحب الكيبوب؟",   
" -  فالتواصل مع الناس تفضل الدردشه كتابياً ولا المكالمات الصوتيه؟",   
" -  في أي سنة بديت تستخدم تطبيقات التواصل الإجتماعي؟",   
" -  شاركنا أغنية غريبة تسمعها دايم؟",
" -  عن ماذا تبحث؟",
" -  تحبني ولا تحب الدراهم؟", 
" -  انا أحبك, وانت؟", 
" -  روحك تنتمي لمكان غير المكان اللي انت عايش فيه؟",
" -  كيف تتصرف لو تغيّر عليك أقرب شخص؟",
" - ‏أغبى نصيحة وصلتك؟",
" - هل اقتربت من تحقيق أحد أهدافك؟",
" - رأيك بمن يستمر في علاقة حب مع شخص وهو يعلم أنه على علاقة حب مع غيره؟",
"‏ - شخصية تاريخية تُحبها؟",
" - ‏كم ساعة نمت؟",
" - أكثر شخصية ممكن تستفزك؟",
" - ‏كلمة لمتابعينك؟",
"‏ - أجمل شعــور؟",
" - أسوأ شعور؟",
" - أقبح العادات المجتمعية في بلدك؟",
" - أحب مُدن بلادك إلى قلبك؟",
"‏ - أصعب أنواع الانتظار؟",
" - ‏ ماذا لو لم يتم اختراع الانترنت؟",
" - هل تعتقد أن امتلاكك لأكثر من صديق أفضل من امتلاكك لصديق واحد؟",
" - ‏ردة فعلك على شخص يقول لك: ما حد درى عنك؟",
" - كتاب تقرأه هذه الأيام؟",
" - ‏هل صحيح الشوق ياخذ من العافية ؟",
" - ‏لماذا الانسان يحب التغيير ؟ حتى وان كان سعيدا !",
"‏ - الاحباط متى ينال منك ؟",
" - ‏بعد مرور اكثر من عام هل مازال هناك من يعتقد ان كورونا كذبة  ؟",
" - هل  تشمت بعدوك وتفرح لضرره مهما كان الضرر قاسيا  ؟",
" - ‏ان كانت الصراحة ستبعد عنك من تحب هل تمتلك الشجاعة للمصارحة  ام لا ؟",
" - ‏ماهو حلك اذا اصابك الارق ؟",
" - ‏ماهو الامر  الذي لايمكن ان تسمح به ؟",
"‏ - هل تلتزم بمبادئك وان كان ثمنها غاليا ؟",
" - ‏ماهو اولى اولوياتك في الحياة ؟",
" - لو خيرت بين ان تعيش وحيدا برفاه  او بين الاحباب بشقاء ماذا ستختار ؟",
" - هل تلجأ الى شخص ينتظر سقوطك وهو الوحيد الذي بامكانه مساعدتك ؟",
" - ‏اكثر شيء تحب امتلاكه ؟",
" - معنى الراحة بالنسبة لك ؟",
" - عرف نفسك بكلمة ؟",
"‏ - لماذا لا ننتبه إلا حينما تسقُط الأشياء ؟",
" - ‏هل شعرت يومًا أنَّك تحتاج لطرح سؤال ما، لكنَّك تعرف في قلبك أنَّك لن تكون قادرًا على التعامل مع الإجابة؟",
]


@app.on_message(
    command(["كت"])
    & ~filters.edited
)
async def mreslam(client: Client, message: Message):
    bar = random.choice(rodod) 
    await message.reply_text(bar)