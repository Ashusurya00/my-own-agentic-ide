"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const axios_1 = __importDefault(require("axios"));
function activate(context) {
    // 🔹 Refactor current file
    const refactorCommand = vscode.commands.registerCommand("agentic-ide.refactorFile", async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage("No active editor");
            return;
        }
        const instruction = await vscode.window.showInputBox({
            prompt: "How should I refactor this file?"
        });
        if (!instruction)
            return;
        const content = editor.document.getText();
        const res = await axios_1.default.post("http://127.0.0.1:8000/edit", {
            content,
            instruction
        });
        const fullRange = new vscode.Range(editor.document.positionAt(0), editor.document.positionAt(content.length));
        editor.edit(editBuilder => {
            editBuilder.replace(fullRange, res.data.result);
        });
    });
    // 🔹 Generate frontend files
    const generateCommand = vscode.commands.registerCommand("agentic-ide.generateFiles", async () => {
        const instruction = await vscode.window.showInputBox({
            prompt: "What do you want to generate?",
            value: "Create a responsive login page using HTML and CSS"
        });
        if (!instruction)
            return;
        await axios_1.default.post("http://127.0.0.1:8000/generate", {
            instruction,
            root: "frontend"
        });
        vscode.window.showInformationMessage("Frontend files generated");
        vscode.commands.executeCommand("workbench.files.action.refreshFilesExplorer");
    });
    context.subscriptions.push(refactorCommand, generateCommand);
}
function deactivate() { }
