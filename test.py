import flet as ft
import datetime

#Pagina Principal
def MainPage(page: ft.Page):
    global switch_parts
    switch_parts = None

    #Definindo informações
    titleMainPage = page.title = 'Serviços e Orçamentos'
    alignmentMainPage = page.vertical_alignment = ft.MainAxisAlignment.START
    scrollAuto = page.auto_scroll = True
    scrollHidden = page.scroll = ft.ScrollMode.HIDDEN
    heightMainPage = page.window.height = 860
    widthMainPage = page.window.width = 420
    resizeMainPage = page.window.resizable = False
    adaptativePage = page.adaptive = True
    getDate = datetime.date.today()
    dateFormated = getDate.strftime('%d/%m/%Y')

    debugEnabled = False

    #Variaveis
    sizeWidth_TextField = 236
    sizeWidth_ValueField = 72

   
    if debugEnabled:
        print(f'Título Principal: {titleMainPage}')
        print(f'Alinhamento Principal: {alignmentMainPage}')
        print(f'Altura Principal: {heightMainPage}')
        print(f'Largura Principal: {widthMainPage}')
        print(f'Tela Redimensionavel: {resizeMainPage}')
        print(f'Scroll Automático: {scrollAuto}')
        print(f'Scroll Escondido: {scrollHidden}')
        print(f'Tela Adaptativa: {adaptativePage}')
    else:
        pass

    
    workHand_Expanded = False
    parts_Expanded = False
    

    #Banco Dados
    workHand_fieldsList = []
    parts_fieldsList = []

    #Funções
    def toggle_editable(e):
        #Função para tornar uma text em textfield
        nonlocal editable_textMechanic
        text_valueMechanic = editable_textMechanic.value
        text_valueMechanic = ''
        editable_textMechanic = ft.TextField(value=text_valueMechanic,label='Mecânico', on_submit=save_textMechanic)
        controls_list.clear()
        controls_list.extend([editable_textMechanic, button_saveMechanic])
        page.update()
    def save_textMechanic(e):
        nonlocal editable_textMechanic
        new_textValue = editable_textMechanic.value.strip()
        if not new_textValue:
            editable_textMechanic.error_text = 'Por favor, preencha este campo.'
            page.update()
        else:
            editable_textMechanic.error_text = ''
            new_textValue_Mechanic = editable_textMechanic.value.capitalize()
            editable_textMechanic = ft.Text(value=f'• Mecânico: {new_textValue_Mechanic}', weight=ft.FontWeight.BOLD, theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
            controls_list.clear()
            controls_list.extend([editable_textMechanic, button_editMechanic])
            page.update()

    #region Mão de Obra
    def toggle_WorkHand(e): #Expandir e Retrair Aba Mão de Obra
        nonlocal workHand_Expanded
        workHand_Expanded = not workHand_Expanded
        if workHand_Expanded and not workHand_fieldsList:
            add_WorkHand_TextFields(None) #Adiciona um Conjunto padrão textfields
        update_menu_WorkHand()
    def update_menu_WorkHand():
        # Limpa Conteudo principal e re-adiciona os controles de acordo com o estado do menu
        columnMain_WorkHand.controls.clear()
        button_WorkHand = ft.ElevatedButton(text='Mão de obra', on_click=toggle_WorkHand)
        columnMain_WorkHand.controls.append(button_WorkHand)
        if workHand_Expanded:
            button_WorkHand.color = ft.colors.RED
            for row in workHand_fieldsList:
                columnMain_WorkHand.controls.append(row)
            columnMain_WorkHand.controls.append(button_addWorkHand)
        page.update()   
    def add_WorkHand_TextFields(e):
        #Cria campos de texto
        text_WorkHandField_Servico = ft.TextField(label='Serviço', width= sizeWidth_TextField, text_size= 12, text_align=ft.TextAlign.LEFT, prefix_text='•')
        text_WorkHandField_Valor = ft.TextField(label='Valor', width= sizeWidth_ValueField, keyboard_type=ft.KeyboardType.NUMBER, text_size= 12, text_align=ft.TextAlign.LEFT, prefix_text='R$')

        button_deleteRow_WorkHand = ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: delete_WorkHand_TextFields(row_WorkHandField)) #Cria botão para deletar linha  
        row_WorkHandField = ft.Row(controls=[text_WorkHandField_Servico, text_WorkHandField_Valor, button_deleteRow_WorkHand],alignment= ft.MainAxisAlignment.CENTER) #Linha com serviço e valor e um botão de exclusão
        workHand_fieldsList.append(row_WorkHandField) #Adiciona Linha ao campo de Fields
        update_menu_WorkHand()
    def delete_WorkHand_TextFields(row_WorkHandField):
        # Remove a linha do campo de Fields
        workHand_fieldsList.remove(row_WorkHandField)
        update_menu_WorkHand()
    

    #region Peças
    def toggle_parts(e):
        nonlocal parts_Expanded
        parts_Expanded = not parts_Expanded
        if parts_Expanded and not parts_fieldsList:
            add_Parts_TextFields(None)
        update_menu_Parts()

    def toggle_DisplayPart(e):
        global switch_parts
        button_Parts.disabled = not e.control.value
        page.update()
    
    def update_menu_Parts():
        # Limpa Conteudo principal e re-adiciona os controles de acordo com o estado do menu
        columnMain_Parts.controls.clear()

        global switch_parts
        switch_value = switch_parts.value if switch_parts else False

        global button_Parts
        button_Parts = ft.ElevatedButton(text='Peças', on_click=toggle_parts, disabled=not switch_value)
        switch_parts = ft.Switch(label='1', value=switch_value, on_change=toggle_DisplayPart)
        
        row_partsControls = ft.Row(controls=[button_Parts, switch_parts], alignment=ft.MainAxisAlignment.CENTER)
        columnMain_Parts.controls.append(row_partsControls)
        
        if parts_Expanded:
            button_Parts.color = ft.colors.RED
            for row in parts_fieldsList:
                columnMain_Parts.controls.append(row)
            columnMain_Parts.controls.append(button_addParts)
        page.update()
    def add_Parts_TextFields(e):
        #Cria campos de texto
        text_Parts_Peca = ft.TextField(label='Peça', width=sizeWidth_TextField, text_size=12, text_align=ft.TextAlign.LEFT, prefix_text='•')
        text_Parts_Valor = ft.TextField(label='Valor', width=sizeWidth_ValueField,keyboard_type=ft.KeyboardType.NUMBER, text_size= 12, text_align=ft.TextAlign.LEFT, prefix_text='R$')

        button_deleteRow_Parts = ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: delete_Parts_TextFields(row_PartsField)) #Cria botão para deletar linha  
        row_PartsField = ft.Row(controls=[text_Parts_Peca, text_Parts_Valor,button_deleteRow_Parts],alignment=ft.MainAxisAlignment.CENTER) #Linha com serviço e valor e um botão de exclusão
        parts_fieldsList.append(row_PartsField) #Adiciona Linha ao campo de Fields
        update_menu_Parts()
    def delete_Parts_TextFields(row_PartsField):
        # Remove a linha do campo de Fields
        parts_fieldsList.remove(row_PartsField)
        update_menu_Parts()
    #endregion
    
    def EnviarInfo(e):
        checkText_Car = text_Car.value.strip()
        if not checkText_Car:
            text_Car.error_text = 'Por favor, coloque o modelo do carro!'
            page.update()
        else:
            text_Car.error_text = ''
            checkText_Car = text_Car.value.capitalize()
            print(titleServiceNotes.value)
            print(infoWorkshop.value)
            print(infoContact.value)
            print(editable_textMechanic.value)
            print(infoDate.value)
            print(f'• Carro: {checkText_Car}')
        
        #Extrair Valores Mao de Obra
        for row in workHand_fieldsList:
            text_Service = row.controls[0].value
            text_Valor = row.controls[1].value
            if text_Service != "":
                print(f'{text_Service}: {text_Valor}')
            else:
                pass
        #Extrair Valores Peças
        for row in parts_fieldsList:
            text_Parts = row.controls[0].value
            text_Valor = row.controls[1].value
            if text_Parts != "":
                print(f'{text_Parts}: {text_Valor}')
            else:
                pass
        
        page.update()
    
    #Labels
    titleServiceNotes = ft.Text('• Nota de Orçamento •', theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,text_align= ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD)
    infoWorkshop = ft.Text('• Oficina:  Mecânica Antunes',weight=ft.FontWeight.BOLD, theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
    infoContact = ft.Text('• Contato: (47) 99955-2048 Pix', weight=ft.FontWeight.BOLD,theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
    editable_textMechanic = ft.Text(value='• Mecanico: Gilberto',weight=ft.FontWeight.BOLD,theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
    infoDate = ft.Text(f'• Data: {dateFormated}',weight=ft.FontWeight.BOLD,theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
    #Widgets
    
    columnMain_WorkHand     = ft.Column(wrap=True, alignment= ft.MainAxisAlignment.CENTER) # Cria a coluna principal para adicionar elementos
    columnMain_Parts        = ft.Column(wrap=True, alignment= ft.MainAxisAlignment.CENTER) # Cria a coluna principal para adicionar elementos

    #Campo Textos Inputs
    text_Car            = ft.TextField(label='Carro',hint_text='Qual o modelo do carro?', width= 320, text_align=ft.TextAlign.CENTER)

    #Botões
    button_editMechanic = ft.IconButton(icon=ft.icons.EDIT, on_click=toggle_editable, icon_size=18)
    button_saveMechanic = ft.IconButton(icon=ft.icons.SAVE, on_click=save_textMechanic, icon_size=18)
    button_addParts     = ft.ElevatedButton(text='+', on_click= add_Parts_TextFields)
    button_addWorkHand  = ft.ElevatedButton(text='+', on_click= add_WorkHand_TextFields)
    button_Send         = ft.ElevatedButton(text='Enviar', on_click=EnviarInfo)
    
    
    controls_list = [editable_textMechanic, button_editMechanic]
    #Build Widgets
    page.add(
        ft.SafeArea(ft.Container(alignment=ft.alignment.top_center),maintain_bottom_view_padding=True),
        ft.ResponsiveRow([titleServiceNotes],alignment=ft.MainAxisAlignment.CENTER),        # • Nota de Orçamento •
        ft.Divider(height=15,thickness=5),                                                  # ----------------------
        ft.ResponsiveRow([infoWorkshop],alignment=ft.MainAxisAlignment.CENTER,height=30),   # • Oficina:  Mec. Antunes
        ft.ResponsiveRow([infoContact],alignment=ft.MainAxisAlignment.CENTER),              # • Contato: (47)99955-2048 Pix 
        ft.Row (controls_list, alignment=ft.MainAxisAlignment.START),                       # • Mecanico: Gilberto 
        ft.ResponsiveRow([infoDate],alignment=ft.MainAxisAlignment.START, height=40),       # • Data 
        ft.ResponsiveRow([text_Car],alignment=ft.MainAxisAlignment.CENTER),                 # • Carro 
        ft.ResponsiveRow([columnMain_WorkHand],alignment=ft.MainAxisAlignment.CENTER),      # • Mão de obra
        ft.ResponsiveRow([columnMain_Parts],alignment=ft.MainAxisAlignment.CENTER),         # • Peças
        ft.Row([button_Send], alignment=ft.MainAxisAlignment.CENTER)
    )
    update_menu_WorkHand()
    update_menu_Parts()



#Rodar o App
ft.app(target=MainPage)
