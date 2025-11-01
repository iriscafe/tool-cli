import subprocess
import sys

def git_prune_useless_branches():
    try:
        subprocess.run(["git", "fetch", "-p"], check=True, capture_output=True)
        
        branches = list_local_branches()
        
        if not branches:
            print("✅ Nenhuma branch órfã encontrada.")
            return None
        
        deleted_count = 0
        
        for branch in branches:
            try:
                subprocess.run(["git", "branch", "-D", branch], check=True, capture_output=True)
                print(f"🗑️  Deletando branch órfã: {branch}")
                deleted_count += 1
            except subprocess.CalledProcessError:
                pass
        
        if deleted_count == 0:
            print("✅ Nenhuma branch órfã encontrada.")
        else:
            print(f"✅ {deleted_count} branch(es) órfã(s) deletada(s).")
        
        return None
        
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando git: {e}", file=sys.stderr)
        if e.stderr:
            print(f"Detalhes: {e.stderr.decode('utf-8') if isinstance(e.stderr, bytes) else e.stderr}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}", file=sys.stderr)
        raise

def list_local_branches():
    try:
        remote_result = subprocess.run(
            ["git", "branch", "-r"],
            check=True,
            capture_output=True,
            text=True
        )
        
        remote_branches = set()
        for branch_remote in remote_result.stdout.strip().split('\n'):
            branch_remote = branch_remote.strip()
            if branch_remote:
                branch_name = branch_remote.replace("origin/", "").strip()
                if branch_name:
                    remote_branches.add(branch_name)
        
        local_result = subprocess.run(
            ["git", "branch", "--format", "%(refname:short)"],
            check=True,
            capture_output=True,
            text=True
        )
        
        local_branches = [
            branch.strip() 
            for branch in local_result.stdout.strip().split('\n') 
            if branch.strip()
        ]
        
        orphan_branches = []
        for branch_local in local_branches:
            if branch_local not in remote_branches:
                orphan_branches.append(branch_local)
        
        return orphan_branches
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando git: {e}", file=sys.stderr)
        if e.stderr:
            print(f"Detalhes: {e.stderr.decode('utf-8') if isinstance(e.stderr, bytes) else e.stderr}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}", file=sys.stderr)
        raise