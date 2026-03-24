import os

with open(r"e:\01_emaus\02. Site\code.html", "r", encoding="utf-8") as f:
    code = f.read()

# Split to get exactly the header and footer
header = code.split("<!-- BEGIN: HeroHeader -->")[0]
# Fix relative links in header so they point to the main page anchors
header = header.replace('href="#', 'href="code.html#')

footer = "  <!-- BEGIN: Footer -->" + code.split("<!-- BEGIN: Footer -->")[1]

# Privacy Policy Content
privacy = """  <!-- BEGIN: Privacy Policy -->
  <section class="py-32 bg-brand-sand/30 min-h-screen" id="politica-de-privacidade">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-12">
      <div class="mb-12">
        <h1 class="font-serif text-4xl text-brand-terracotta mb-4">Política de Privacidade</h1>
        <div class="w-16 h-1 bg-brand-gold rounded-full mb-6"></div>
        <p class="text-stone-500 text-sm">Última atualização: Março de 2026</p>
      </div>

      <div class="prose prose-stone max-w-none text-stone-600 space-y-6 bg-white p-8 md:p-12 rounded-custom shadow-sm border border-brand-beige">
        <p class="text-lg">
          O <strong>EMAUS Movimento de Evangelização</strong> valoriza e respeita a sua privacidade. Esta Política de Privacidade descreve como coletamos, usamos, armazenamos e protegemos as suas informações pessoais ao interagir com o nosso site e participar de nossos encontros, em conformidade com a da Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018).
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">1. Coleta de Informações</h3>
        <p>
          Coletamos informações pessoais que você nos fornece voluntariamente quando:
        </p>
        <ul class="list-disc pl-5 space-y-2">
          <li>Se inscreve para participar de nossos retiros ou encontros.</li>
          <li>Entra em contato conosco através de nossos canais de comunicação (como WhatsApp ou e-mail).</li>
          <li>Realiza doações voluntárias ao movimento.</li>
        </ul>
        <p>
          Os dados coletados podem incluir, mas não estão limitados a: nome completo, telefone, e-mail e informações básicas necessárias para a organização logística dos nossos retiros.
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">2. Uso das Informações</h3>
        <p>
          Utilizamos as suas informações exclusivamente para as seguintes finalidades:
        </p>
        <ul class="list-disc pl-5 space-y-2">
          <li>Organizar, comunicar e coordenar a sua participação nos encontros do EMAUS.</li>
          <li>Enviar atualizações, novidades e informações importantes sobre o movimento.</li>
          <li>Responder as suas dúvidas e solicitações.</li>
          <li>Processar doações (quando aplicável, repassando aos prestadores de serviço financeiro).</li>
        </ul>
        <p class="font-bold text-brand-orange">Nós nunca vendemos ou comercializamos os seus dados pessoais.</p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">3. Compartilhamento de Dados</h3>
        <p>
          As suas informações são acessadas apenas por membros da organização do EMAUS que necessitem delas para a realização das atividades propostas. Nós não compartilhamos os seus dados com terceiros, exceto quando indispensável para a prestação de serviços (como plataformas de pagamento, as quais possuem suas próprias políticas de privacidade) ou por exigência legal.
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">4. Gravação de Imagem e Voz</h3>
        <p>
          Durante os nossos retiros e ações evangelizadoras, podemos registrar fotos e vídeos para compor nossa "Galeria de Momentos", com o intuito único de divulgação das obras do movimento. Ao participar voluntariamente de nossos encontros, você consente com a utilização da sua imagem nesses registros, que serão divulgados apenas em nossos canais oficiais e apresentações do grupo. Caso você não deseje ter a sua imagem divulgada, pedimos a gentileza de comunicar a nossa equipe no momento de sua chegada.
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">5. Seus Direitos</h3>
        <p>
          Conforme a LGPD, você possui o direito de:
        </p>
        <ul class="list-disc pl-5 space-y-2">
          <li>Confirmar a existência do tratamento de dados.</li>
          <li>Acessar os seus dados.</li>
          <li>Solicitar a correção de dados incompletos, inexatos ou desatualizados.</li>
          <li>Solicitar a exclusão de seus dados pessoais, sempre que possível legalmente.</li>
          <li>Revogar o seu consentimento.</li>
        </ul>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">6. Contato</h3>
        <p>
          Se você tiver alguma dúvida sobre esta Política de Privacidade ou desejar exercer os seus direitos, por favor, entre em contato conosco pelos links disponíveis na seção "Como Apoiar" de nosso site ou conversando com a equipe organizadora durante o encontro.
        </p>
      </div>
    </div>
  </section>
  <!-- END: Privacy Policy -->
"""

# Terms of Use Content
terms = """  <!-- BEGIN: Terms of Use -->
  <section class="py-32 bg-brand-sand/30 min-h-screen" id="termos-de-uso">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-12">
      <div class="mb-12">
        <h1 class="font-serif text-4xl text-brand-terracotta mb-4">Termos de Uso</h1>
        <div class="w-16 h-1 bg-brand-gold rounded-full mb-6"></div>
        <p class="text-stone-500 text-sm">Última atualização: Março de 2026</p>
      </div>

      <div class="prose prose-stone max-w-none text-stone-600 space-y-6 bg-white p-8 md:p-12 rounded-custom shadow-sm border border-brand-beige">
        <p class="text-lg">
          Bem-vindo ao <strong>EMAUS Movimento de Evangelização</strong>. Ao acessar e utilizar nosso site, você concorda com os seguintes termos e condições de uso. Pedimos que leia atentamente antes de continuar a navegação.
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">1. Uso de Nosso Site</h3>
        <p>
          O conteúdo deste site tem o propósito de divulgar as ações evangelizadoras, retiros e encontros do movimento EMAUS. Você concorda em utilizar este site apenas para fins legais e de maneira que não infrinja os direitos de terceiros, não restrinja nem iniba a utilização por parte de outras pessoas.
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">2. Direitos Autorais e Propriedade Intelectual</h3>
        <p>
          Todo o material contido neste site, incluindo textos, logotipos, imagens (fotos e vídeos) e design, é de propriedade do EMAUS ou utilizado com a devida autorização. O conteúdo pode ser compartilhado para fins de evangelização e divulgação do grupo, desde que atribuídos os devidos créditos, e <strong>nunca para fins comerciais</strong>.
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">3. Participação e Doações</h3>
        <p>
          A inscrição em nossos encontros e a realização de doações através dos links disponibilizados ocorrem de forma voluntária. O EMAUS utiliza canais seguros para a comunicação (como nossos canais oficiais de WhatsApp), mas os usuários são inteiramente responsáveis pela veracidade das informações ali fornecidas e pela conferência dos dados antes de efetuarem transações financeiras.
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">4. Isenção de Responsabilidade</h3>
        <p>
          O EMAUS busca manter as informações do site sempre atualizadas (como datas de encontros e eventos). Porém, nos reservamos o direito de alterar agendas, locais e formatos de encontros por razões de força maior, sem aviso prévio. Os links externos apresentados em nosso site (como páginas de redirecionamento ou WhatsApp) são fornecidos para a conveniência do usuário; não nos responsabilizamos pelas práticas e políticas dessas plataformas parceiras.
        </p>

        <h3 class="font-serif text-2xl text-stone-900 mt-10 mb-4 border-b pb-2">5. Acordo Aceito</h3>
        <p>
          O uso contínuo deste site constitui a sua aceitação destes Termos de Uso bem como de nossa <a href="privacidade.html" class="text-brand-orange hover:underline font-bold">Política de Privacidade</a>.
        </p>
      </div>
    </div>
  </section>
  <!-- END: Terms of Use -->
"""

# Write to arquivos
with open(r"e:\01_emaus\02. Site\privacidade.html", "w", encoding="utf-8") as f:
    f.write(header + privacy + footer)

with open(r"e:\01_emaus\02. Site\termos.html", "w", encoding="utf-8") as f:
    f.write(header + terms + footer)

print("LGPD Pages HTML generated cleanly.")
