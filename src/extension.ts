import * as vscode from "vscode";
import axios from "axios";

export function activate(context: vscode.ExtensionContext) {

    // 🔹 Refactor current file
    const refactorCommand = vscode.commands.registerCommand(
        "agentic-ide.refactorFile",
        async () => {
            const editor = vscode.window.activeTextEditor;
            if (!editor) {
                vscode.window.showErrorMessage("No active editor");
                return;
            }

            const instruction = await vscode.window.showInputBox({
                prompt: "How should I refactor this file?"
            });
            if (!instruction) return;

            const content = editor.document.getText();

            const res = await axios.post("http://127.0.0.1:8000/edit", {
                content,
                instruction
            });

            const fullRange = new vscode.Range(
                editor.document.positionAt(0),
                editor.document.positionAt(content.length)
            );

            editor.edit(editBuilder => {
                editBuilder.replace(fullRange, res.data.result);
            });
        }
    );

    // 🔹 Generate frontend files
    const generateCommand = vscode.commands.registerCommand(
        "agentic-ide.generateFiles",
        async () => {
            const instruction = await vscode.window.showInputBox({
                prompt: "What do you want to generate?",
                value: "Create a responsive login page using HTML and CSS"
            });

            if (!instruction) return;

            await axios.post("http://127.0.0.1:8000/generate", {
                instruction,
                root: "frontend"
            });

            vscode.window.showInformationMessage("Frontend files generated");
            vscode.commands.executeCommand("workbench.files.action.refreshFilesExplorer");
        }
    );

    context.subscriptions.push(refactorCommand, generateCommand);
}

export function deactivate() { }
