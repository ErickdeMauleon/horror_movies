import streamlit as st
from streamlit_player import st_player


st.title("Historia del cine de terror")

st.header("Primeras películas de terror")
st.markdown("""<div style="text-align: justify;">A finales del siglo XIX, pioneros del cine como Georges Méliès comenzaron a experimentar con efectos especiales 
y trucos visuales para crear películas que asustaran y sorprendieran a la audiencia. "La mansión del diablo"(1896) se considera una de las primeras películas de terror.
En ella, un murciélago se convierte en demonio, el cual aparece en la habitación de un hombre y le hace aparecer una serie de monstruos
tales como brujas o fantasmas.</div>""", unsafe_allow_html=True)

st_player("https://www.youtube.com/watch?v=0FCFYFK08D4")

st.header("Cine mudo estadounidense")
st.markdown("""<div style="text-align: justify;">El cine mudo fue el primer medio en el que se desarrolló el género de terror. Las películas mudas se caracterizaban por la ausencia de diálogos y la presencia de subtítulos explicativos.
Las películas mudas de terror más destacadas son:
</div>
""", unsafe_allow_html=True)
st.markdown("""
- Frankenstein (1910)
- Dr. Jekyll and Mr. Hyde (1920)
- El fantasma de la ópera (1925)
- El gabinete de las figuras de cera (1923)
""", unsafe_allow_html=True)
st.header("El expresionismo alemán")
a, b = st.columns(2)
img_url = "https://historia-arte.com/_/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpbSI6WyJcL2FydHdvcmtcL2ltYWdlRmlsZVwvM2NlZGZhODQxZjA1OGUwY2YzODc1YzUzODQ3MjRjODYuanBnIiwicmVzaXplLDgwMCJdfQ.Xqwbi8jS3mI9yahMsywWItHF3sOKzcsfiSrq1ooY6F4.jpg"
a.image(img_url, caption="Naturaleza muerta de máscaras (Emil Nolde)", use_column_width=True)
b.write("""<div style="text-align: justify;">El expresionismo alemán fue un movimiento artístico que se desarrolló en Alemania a principios del siglo XX. 
Abrazaban una visión más subjetiva que permitiera transmitir la desesperación, la angustia, el miedo o la locura que respondían al punto de vista de personajes torturados.
El expresionismo alemán se caracterizaba por el uso de la luz y la sombra, la distorsión de la realidad y la exageración de las emociones.
Este movimiento artístico es resultado en buena parte por la situación política y social de Alemania en la época, marcada por perder la Primera Guerra Mundial y la crisis económica.
</div>""", unsafe_allow_html=True)
b.markdown("""
- El Golem (1915)
- El gabinete del Dr. Caligari (1920)            
- Nosferatu (1922)           
- El estudiante de Praga (1926) 
- El gato y el canario (1927)
""", unsafe_allow_html=True)
st.subheader("El gabinete del Dr. Caligari (1920)")
st.markdown("""<div style="text-align: justify;">El gabinete del Dr. Caligari es una película muda alemana de terror dirigida por Robert Wiene.
La película se desarrolla en un pueblo de Holstenwall, donde un misterioso hipnotizador, el Dr. Caligari, llega al pueblo con su espectáculo de sonámbulos.
Uno de los sonámbulos, Cesare, será el autor de una serie de asesinatos que aterrorizarán al pueblo. Estubo inspirada en un hecho policial sucedido en Hamburgo.
La idea de los guionistas era crear una película que reflejara la situación política y social de Alemania en la época, Janowitz y Mayer querían plasmar
una metáfora de las atrocidades cometidas por el estado alemán durante la Guerra. Janowitz en especial estaba muy resentido con el gobierno alemán por haberle
obligado a alistarse en el ejército y por haberle enviado al frente. La escenografía de la película es muy característica, con calles y edificios torcidos, irreales y
pesadillescos. Otro elemento característico de la película es el uso de la luz y la sombra, esencialmente por su falta de luz, las sombras fueron pintadas 
a mano en el decorado, debido a la falta de luz en los estudios de filmación. 
</div>""", unsafe_allow_html=True)
            
            
            

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Frankenstein (1910)"
                                  , "Dr. Jekyll and Mr. Hyde (1920)"
                                  , "El gabinete del Dr. Caligari (1920)", "Nosferatu (1922)", "El gato y el canario (1927)"])

with tab1:
    st_player("https://www.youtube.com/watch?v=67ENQibFW9w")
with tab2:
    st_player("https://www.youtube.com/watch?v=kjQaAK5Vof4")
with tab3:
    st_player("https://www.youtube.com/watch?v=WmlaUHqQNao")
with tab4:
    st_player("https://www.youtube.com/watch?v=FC6jFoYm3xs")
with tab5:
    st_player("https://www.youtube.com/watch?v=PzztINNTIos")

st.header("Monstruos de Universal Studios")
c, d = st.columns(2)
filename = "bela_lugosi.png"
d.image(filename, caption="Bela Lugosi como Drácula", use_column_width=True)
filename = "invisible_man.jpg"
d.image(filename, caption="El hombre invisible", use_column_width=True)
c.markdown("""<div style="text-align: justify;">Universal Studios es un estudio de cine estadounidense fundado en 1912 por Carl Laemmle.
En 1923, Universal Studios estrenó su primera película de terror, "El jorobado de Notre Dame", protagonizada por Lon Chaney.
En la década de 1930, Universal Pictures creó un universo cinematográfico de monstruos que incluía a personajes icónicos como:
</div>""", unsafe_allow_html=True)
c.markdown("""
- Drácula (1931)
- Frankenstein (1931)
- La momia (1932)
- El hombre invisible (1933)
- La novia de Frankenstein (1935)
- El hombre lobo (1941)
""", unsafe_allow_html=True)

st.header("Cine mexicano")
e, f = st.columns(2)
f.markdown("""<div style="text-align: justify;">El cine de terror mexicano se desarrolló desde la década de 1930. El cine de terror mexicano se caracterizó por la presencia de monstruos
y personajes sobrenaturales que aterrorizaban a la audiencia. El cine de terror mexicano se desarrolló en la época de oro del cine mexicano.
Tenemos que destacar a directores de cine de terror mexicano como Ramón Peón, Juan Bustillo Oro, Fernando Méndez o Chano Urueta.
</div>""", unsafe_allow_html=True)
f.markdown("""
- El grito de la muerte (1933, Ramón Peón)
- La llorona (1933, Ramón Peón)
- El fantasma del convento (1934, Juan Bustillo Oro)
- El hombre sin rostro (1950, Fernando de Fuentes)
- El monstruo resucitado (1953, Chano Urueta)
- El vampiro (1957, Fernando Méndez)
- Hasta el viento tiene miedo (1968)
""", unsafe_allow_html=True)
e.image("monstruo_resucitado.png", caption="Monstruo resucitado (1953)", use_column_width=True)
e.image("el_vampiro.png", caption="Germán Robles como El vampiro (1957)", use_column_width=True)

            
t1, t2, t3 = st.tabs(["La llorona (1933)", "El fantasma del convento (1934)", "Hasta el viento tiene miedo (1968)"])

with t1:
    st_player("https://www.youtube.com/watch?v=vwtlaAVLJrM")
with t2:
    st_player("https://www.youtube.com/watch?v=fMDAsy4_EeA")
with t3:
    st_player("https://www.youtube.com/watch?v=04Ak42Qkgc0")

# st_player("https://www.youtube.com/watch?v=tuwWb2wsyMo")
