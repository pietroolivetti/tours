import streamlit as st
import edge_tts
import io
import re
import subprocess
from scripts import *

def sentences(sent, names):
    for i in range(len(sent)):
        st.write(sent[i])
        st.audio(f'{names[i]}.mp3')

#cmd = ["edge-tts", "--rate=-15%" , "--voice", "nl-NL-MaartenNeural", "--text", i, "--write-media", f"audios/{count}.mp3"]

 # Create a dropdown menu using selectbox
choice_lang =  {'Português': 'pt-BR-AntonioNeural', 'English': 'en-US-AriaNeural', 'Italiano': 'it-IT-GiuseppeNeural', 'Español': 'es-AR-ElenaNeural', 'Français': 'fr-FR-HenriNeural', 'Deutsch': 'de-DE-KillianNeural'}
selected_lang = st.selectbox('Select a language:', choice_lang, index=0)
st.write(f"You've selected: {selected_lang}")
#tabspt = ["Entrada", "História", "Vinificação", "Maturação", "Tipologia", "Vale do Douro"]
    
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Entrada", "História", "Vinificação", "Maturação", "Tipologia", "Vale do Douro", "Degustação"])

if selected_lang == 'Português':

    with tab1:

        st.write(pt1)
       #cmd = ["edge-tts", "--voice", "pt-BR-AntonioNeural", "--text", pt1, "--write-media", f"pt1.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"pt1.mp3")
        
        with st.expander('Frases'):
            sentences(pt1_list, pt1_audios)

    with tab2:
        st.write(pt2)
       #cmd = ["edge-tts", "--voice", "pt-BR-AntonioNeural", "--text", pt2, "--write-media", f"pt2.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"pt2.mp3")
        
        with st.expander('Frases'):
            sentences(pt2_list, pt2_audios)

    with tab3:
        st.write(pt3)
       #cmd = ["edge-tts", "--voice", "pt-BR-AntonioNeural", "--text", pt3, "--write-media", f"pt3.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"pt3.mp3")
        
        with st.expander('Frases'):
            sentences(pt3_list, pt3_audios)
            
    with tab4:
        st.write(pt4)
       #cmd = ["edge-tts", "--voice", "pt-BR-AntonioNeural", "--text", pt4, "--write-media", f"pt4.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"pt4.mp3")
        
        with st.expander('Frases'):
            sentences(pt4_list, pt4_audios)
        
    with tab5:
        st.write(pt5)
       #cmd = ["edge-tts", "--voice", "pt-BR-AntonioNeural", "--text", pt5, "--write-media", f"pt5.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"pt5.mp3")
        
        with st.expander('Frases'):
            sentences(pt5_list, pt5_audios)
        
    with tab6:
        st.write(pt6)
       #cmd = ["edge-tts", "--voice", "pt-BR-AntonioNeural", "--text", pt6, "--write-media", f"pt6.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"pt6.mp3")

        with st.expander('Frases'):
            sentences(pt6_list, pt6_audios)
            
    with tab7:
        with st.expander('Clássica'):
            st.title('Fine White')
            st.write(pt_finewhite)
            st.audio('pt_finewhite.mp3')

            st.title('Jockey Club')
            st.write(pt_jockeyclub)
            st.audio('pt_jockeyclub.mp3')
            
        with st.expander('Premium'):
            st.title('Fine White')
            st.write(pt_finewhite)
            st.audio('pt_finewhite.mp3')

            st.title('LBV 2019')
            st.write(pt_lbv2019)
            st.audio('pt_lbv2019.mp3')
            
            st.title('Tawny 10 anos')
            st.write(pt_tawny10)
            st.audio('pt_tawny10.mp3')
            
        with st.expander('Exclusive'):
            st.title('Tawny 10 anos')
            st.write(pt_tawny10)
            st.audio('pt_tawny10.mp3')

            st.title('Colheita 2008')
            st.write(pt_colheita2008)
            st.audio('pt_colheita2008.mp3')
            
            st.title('Tawny 20 anos')
            st.write(pt_tawny20)
            st.audio('pt_tawny20.mp3')
            
        with st.expander('Tawny Experience'):
            st.title('Tawny')
            st.write(pt_finewhite)
            st.audio('pt_finewhite.mp3')

            st.title('Vintage 2012')
            st.write(pt_vintage2012)
            st.audio('pt_vintage2012.mp3')
            
            st.title('Colheita 2008')
            st.write(pt_colheita2008)
            st.audio('pt_colheita2008.mp3')
            
        with st.expander('Chocolate and Cheese'):
            st.title('LBV 2019')
            st.write(pt_lbv2019)
            st.audio('pt_lbv2019.mp3')

            st.title('Vintage 2012')
            st.write(pt_vintage2012)
            st.audio('pt_vintage2012.mp3')
            
            st.title('Colheita 2002')
            st.write(pt_colheita2002)
            st.audio('pt_colheita2002.mp3')
            
            
if selected_lang == 'Español':

    with tab1:
        st.write(es1)
       #cmd = ["edge-tts", "--voice", "es-AR-ElenaNeural", "--text", es1, "--write-media", f"es1.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"es1.mp3")

    with tab2:
        st.write(es2)
       #cmd = ["edge-tts", "--voice", "es-AR-ElenaNeural", "--text", es2, "--write-media", f"es2.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"es2.mp3")

    with tab3:
        st.write(es3)
       #cmd = ["edge-tts", "--voice", "es-AR-ElenaNeural", "--text", es3, "--write-media", f"es3.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"es3.mp3")
        
    with tab4:
        st.write(es4)
       #cmd = ["edge-tts", "--voice", "es-AR-ElenaNeural", "--text", es4, "--write-media", f"es4.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"es4.mp3")
        
    with tab5:
        st.write(es5)
       #cmd = ["edge-tts", "--voice", "es-AR-ElenaNeural", "--text", es5, "--write-media", f"es5.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"es5.mp3")
        
    with tab6:
        st.write(es6)
       #cmd = ["edge-tts", "--voice", "es-AR-ElenaNeural", "--text", es6, "--write-media", f"es6.mp3"]
        ##subprocess.run(cmd)
        st.audio(f"es6.mp3")
        
    with tab7:
        with st.expander('Clássica'):
            st.title('Fine White')
            st.write(es_finewhite)
            st.audio('es_finewhite.mp3')

            st.title('Jockey Club')
            st.write(es_jockeyclub)
            st.audio('es_jockeyclub.mp3')
            
        with st.expander('Premium'):
            st.title('Fine White')
            st.write(es_finewhite)
            st.audio('es_finewhite.mp3')

            st.title('LBV 2019')
            st.write(es_lbv2019)
            st.audio('es_lbv2019.mp3')
            
            st.title('Tawny 10 anos')
            st.write(es_tawny10)
            st.audio('es_tawny10.mp3')
            
        with st.expander('Exclusive'):
            st.title('Tawny 10 anos')
            st.write(es_tawny10)
            st.audio('es_tawny10.mp3')

            st.title('Colheita 2008')
            st.write(es_colheita2008)
            st.audio('es_colheita2008.mp3')
            
            st.title('Tawny 20 anos')
            st.write(es_tawny20)
            st.audio('es_tawny20.mp3')
            
        with st.expander('Tawny Experience'):
            st.title('Tawny')
            st.write(es_finewhite)
            st.audio('es_finewhite.mp3')

            st.title('Vintage 2012')
            st.write(es_vintage2012)
            st.audio('es_vintage2012.mp3')
            
            st.title('Colheita 2008')
            st.write(es_colheita2008)
            st.audio('es_colheita2008.mp3')
            
        with st.expander('Chocolate and Cheese'):
            st.title('LBV 2019')
            st.write(es_lbv2019)
            st.audio('es_lbv2019.mp3')

            st.title('Vintage 2012')
            st.write(es_vintage2012)
            st.audio('es_vintage2012.mp3')
            
            st.title('Colheita 2002')
            st.write(es_colheita2002)
            st.audio('es_colheita2002.mp3')

if selected_lang == 'Italiano':

    with tab1:
        st.write(it1)
       #cmd = ["edge-tts", "--voice", "it-IT-GiuseppeNeural", "--text", it1, "--write-media", f"it1.mp3"]
        #subprocess.run(cmd)
        st.audio(f"it1.mp3")

    with tab2:
        st.write(it2)
       #cmd = ["edge-tts", "--voice", "it-IT-GiuseppeNeural", "--text", it2, "--write-media", f"it2.mp3"]
        #subprocess.run(cmd)
        st.audio(f"it2.mp3")

    with tab3:
        st.write(it3)
       #cmd = ["edge-tts", "--voice", "it-IT-GiuseppeNeural", "--text", it3, "--write-media", f"it3.mp3"]
        #subprocess.run(cmd)
        st.audio(f"it3.mp3")

    with tab4:
        st.write(it4)
       #cmd = ["edge-tts", "--voice", "it-IT-GiuseppeNeural", "--text", it4, "--write-media", f"it4.mp3"]
        #subprocess.run(cmd)
        st.audio(f"it4.mp3")

    with tab5:
        st.write(it5)
       #cmd = ["edge-tts", "--voice", "it-IT-GiuseppeNeural", "--text", it5, "--write-media", f"it5.mp3"]
        #subprocess.run(cmd)
        st.audio(f"it5.mp3")

    with tab6:
        st.write(it6)
       #cmd = ["edge-tts", "--voice", "it-IT-GiuseppeNeural", "--text", it6, "--write-media", f"it6.mp3"]
        #subprocess.run(cmd)
        st.audio(f"it6.mp3")

if selected_lang == 'Français':

    with tab1:
        st.write(fr1)
       #cmd = ["edge-tts", "--voice", "fr-FR-HenriNeural", "--text", fr1, "--write-media", f"fr1.mp3"]
        #subprocess.run(cmd)
        st.audio(f"fr1.mp3")

    with tab2:
        st.write(fr2)
       #cmd = ["edge-tts", "--voice", "fr-FR-HenriNeural", "--text", fr2, "--write-media", f"fr2.mp3"]
        #subprocess.run(cmd)
        st.audio(f"fr2.mp3")

    with tab3:
        st.write(fr3)
       #cmd = ["edge-tts", "--voice", "fr-FR-HenriNeural", "--text", fr3, "--write-media", f"fr3.mp3"]
        #subprocess.run(cmd)
        st.audio(f"fr3.mp3")

    with tab4:
        st.write(fr4)
       #cmd = ["edge-tts", "--voice", "fr-FR-HenriNeural", "--text", fr4, "--write-media", f"fr4.mp3"]
        #subprocess.run(cmd)
        st.audio(f"fr4.mp3")

    with tab5:
        st.write(fr5)
       #cmd = ["edge-tts", "--voice", "fr-FR-HenriNeural", "--text", fr5, "--write-media", f"fr5.mp3"]
        #subprocess.run(cmd)
        st.audio(f"fr5.mp3")

    with tab6:
        st.write(fr6)
       #cmd = ["edge-tts", "--voice", "fr-FR-HenriNeural", "--text", fr6, "--write-media", f"fr6.mp3"]
        #subprocess.run(cmd)
        st.audio(f"fr6.mp3")


if selected_lang == 'English':

    with tab1:
        st.write(en1)
       #cmd = ["edge-tts", "--voice", "en-US-AriaNeural", "--text", en1, "--write-media", f"en1.mp3"]
        #subprocess.run(cmd)
        st.audio(f"en1.mp3")

    with tab2:
        st.write(en2)
       #cmd = ["edge-tts", "--voice", "en-US-AriaNeural", "--text", en2, "--write-media", f"en2.mp3"]
        #subprocess.run(cmd)
        st.audio(f"en2.mp3")

    with tab3:
        st.write(en3)
       #cmd = ["edge-tts", "--voice", "en-US-AriaNeural", "--text", en3, "--write-media", f"en3.mp3"]
        #subprocess.run(cmd)
        st.audio(f"en3.mp3")

    with tab4:
        st.write(en4)
       #cmd = ["edge-tts", "--voice", "en-US-AriaNeural", "--text", en4, "--write-media", f"en4.mp3"]
        #subprocess.run(cmd)
        st.audio(f"en4.mp3")

    with tab5:
        st.write(en5)
       #cmd = ["edge-tts", "--voice", "en-US-AriaNeural", "--text", en5, "--write-media", f"en5.mp3"]
        #subprocess.run(cmd)
        st.audio(f"en5.mp3")

    with tab6:
        st.write(en6)
       #cmd = ["edge-tts", "--voice", "en-US-AriaNeural", "--text", en6, "--write-media", f"en6.mp3"]
        #subprocess.run(cmd)
        st.audio(f"en6.mp3")
