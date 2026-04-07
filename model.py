from fileinput import filename

import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def aneh_kamu(ctx):
    await ctx.send(f'yang bilang {bot.user} aneh, artinya dia yang aneh, aku tau kamu Evan, hahahahaha')

@bot.command()
async def kamu_tau_mesin(ctx):
    await ctx.send(f'tau lah ada mesin onet enggine, mesin diesel, mesin bensin, mesin jet, mesin uap, mesin cuci, mesin jahit, mesin tik, mesin fotocopy, mesin ATM, mesin kasir, mesin canggih lainnya')



@bot.command()
async def data(ctx):
    await ctx.send(f"Tobias tolong jangan cekek orang dan aneh-aneh ya, kalau setuju ketik ($setuju) ya!")


@bot.command()
async def setuju(ctx):
    await ctx.send(f"Terima kasih {ctx.author.mention} udah setuju!")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for att in ctx.message.attachments:
            file_name = att.filename
            file_url = att.url
            
            # Kirim pesan bahwa bot mulai memproses
            await ctx.send(f"📥 **Menerima gambar:** {file_name}")
            
            try:
                # Simpan gambar
                await att.save(f"./{file_name}")
                await ctx.send(f"💾 **Gambar tersimpan**")
                
                # Panggil AI
                await ctx.send(f"🧠 **Memproses dengan AI...**")
                result = get_class(
                    model_path="./keras_model.h5", 
                    labels_path="./labels.txt", 
                    image_path=f"./{file_name}"
                )
                
                # Kirim hasil
                await ctx.send(f"🤖 **Hasil:** {result}")
                
            except FileNotFoundError as e:
                await ctx.send(f"❌ **File tidak ditemukan:** {str(e)}\nPastikan `keras_model.h5` dan `labels.txt` ada!")
            except Exception as e:
                await ctx.send(f"❌ **Error:** {str(e)}")
                # Cetak error lengkap ke terminal biar kelihatan
                import traceback
                traceback.print_exc()
            
            await ctx.send(f'🔗 {file_url}')
    else:
        await ctx.send("❌ Please attach an image for classification.")



bot.run("")


